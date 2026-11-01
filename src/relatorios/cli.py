"""Linha de comando: lê as planilhas, gera o relatório e, opcionalmente, envia por e-mail."""

from __future__ import annotations

import argparse
import logging
import sys
from datetime import date
from pathlib import Path

from relatorios.analysis import filter_month, summarize
from relatorios.email_report import (
    EmailConfigError,
    SmtpSettings,
    build_html_summary,
    build_message,
    load_env_file,
    send_message,
)
from relatorios.excel_report import write_excel_report
from relatorios.formatting import format_brl
from relatorios.loader import DataError, load_sales

logger = logging.getLogger("relatorios")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="relatorios",
        description="Consolida planilhas de vendas e gera um relatório em Excel e HTML.",
    )
    parser.add_argument("--entrada", type=Path, required=True, help="pasta com os arquivos .csv/.xlsx")
    parser.add_argument("--saida", type=Path, default=Path("saida"), help="pasta de saída (padrão: ./saida)")
    parser.add_argument("--mes", help="considera só um mês, no formato AAAA-MM")
    parser.add_argument("--top", type=int, default=10, help="quantidade de produtos no ranking (padrão: 10)")
    parser.add_argument(
        "--enviar-email",
        action="store_true",
        help="envia o relatório por e-mail usando as variáveis SMTP_* (ou um arquivo .env)",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="mostra mensagens de depuração")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-7s %(message)s",
        datefmt="%H:%M:%S",
    )

    try:
        sales = load_sales(args.entrada).sales
    except DataError as error:
        logger.error("%s", error)
        return 1

    if args.mes:
        try:
            sales = filter_month(sales, args.mes)
        except ValueError:
            logger.error("Mês inválido: %s (use AAAA-MM, por exemplo 2026-10).", args.mes)
            return 1

    if sales.empty:
        logger.error("Nenhuma venda encontrada para o período informado.")
        return 1

    summary = summarize(sales, top_products=args.top)
    suffix = args.mes or date.today().isoformat()
    excel_path = write_excel_report(summary, sales, args.saida / f"relatorio_vendas_{suffix}.xlsx")
    html_body = build_html_summary(summary)
    html_path = args.saida / f"relatorio_vendas_{suffix}.html"
    html_path.write_text(html_body, encoding="utf-8")

    logger.info(
        "Faturamento: %s em %d vendas. Relatório salvo em %s",
        format_brl(summary.total_revenue),
        summary.total_sales,
        excel_path,
    )

    if args.enviar_email:
        return _send(summary.period_start, summary.period_end, html_body, excel_path)
    return 0


def _send(start: date, end: date, html_body: str, attachment: Path) -> int:
    load_env_file(Path(".env"))
    try:
        settings = SmtpSettings.from_env()
    except EmailConfigError as error:
        logger.error("%s (veja o arquivo .env.exemplo)", error)
        return 1

    subject = f"Relatório de vendas | {start:%d/%m/%Y} a {end:%d/%m/%Y}"
    try:
        send_message(settings, build_message(settings, subject, html_body, attachment))
    except OSError as error:  # smtplib.SMTPException herda de OSError
        logger.error("Falha ao enviar e-mail: %s", error)
        return 1

    logger.info("Relatório enviado para %s.", ", ".join(settings.recipients))
    return 0


if __name__ == "__main__":
    sys.exit(main())
