"""Resumo em HTML e envio do relatório por e-mail via SMTP."""

from __future__ import annotations

import html
import mimetypes
import os
import smtplib
import ssl
from collections.abc import Mapping
from dataclasses import dataclass
from email.message import EmailMessage
from pathlib import Path

import pandas as pd

from relatorios.analysis import SalesSummary
from relatorios.formatting import format_brl, format_percent

REQUIRED_ENV_VARS = ("SMTP_HOST", "SMTP_USUARIO", "SMTP_SENHA", "RELATORIO_DESTINATARIOS")


class EmailConfigError(Exception):
    """Configuração de e-mail ausente ou inválida."""


@dataclass(frozen=True)
class SmtpSettings:
    host: str
    port: int
    username: str
    password: str
    sender: str
    recipients: list[str]

    @classmethod
    def from_env(cls, env: Mapping[str, str] = os.environ) -> SmtpSettings:
        missing = [name for name in REQUIRED_ENV_VARS if not env.get(name)]
        if missing:
            raise EmailConfigError(f"Variáveis de ambiente ausentes: {', '.join(missing)}")

        try:
            port = int(env.get("SMTP_PORTA", "587"))
        except ValueError as error:
            raise EmailConfigError("SMTP_PORTA deve ser um número.") from error

        recipients = [r.strip() for r in env["RELATORIO_DESTINATARIOS"].split(",") if r.strip()]
        return cls(
            host=env["SMTP_HOST"],
            port=port,
            username=env["SMTP_USUARIO"],
            password=env["SMTP_SENHA"],
            sender=env.get("SMTP_REMETENTE") or env["SMTP_USUARIO"],
            recipients=recipients,
        )


def load_env_file(path: Path, env: dict[str, str] | None = None) -> None:
    """Carrega um arquivo ``.env`` simples (``CHAVE=valor``) sem sobrescrever variáveis já definidas."""
    target = os.environ if env is None else env
    if not path.is_file():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        target.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def build_html_summary(summary: SalesSummary, top: int = 5) -> str:
    period = f"{summary.period_start:%d/%m/%Y} a {summary.period_end:%d/%m/%Y}"
    kpis = [
        ("Faturamento total", format_brl(summary.total_revenue)),
        ("Número de vendas", f"{summary.total_sales:,}".replace(",", ".")),
        ("Itens vendidos", f"{summary.total_items:,}".replace(",", ".")),
        ("Ticket médio", format_brl(summary.average_ticket)),
    ]
    kpi_rows = "".join(
        f"<tr><td style='padding:6px 12px'>{label}</td>"
        f"<td style='padding:6px 12px;font-weight:bold;text-align:right'>{value}</td></tr>"
        for label, value in kpis
    )

    return f"""<html>
<body style="font-family:Arial,sans-serif;color:#222">
  <h2 style="color:#1F4E78">Relatório de vendas</h2>
  <p>Período: <strong>{period}</strong></p>
  <table style="border-collapse:collapse;background:#F2F6FA">{kpi_rows}</table>
  <h3>Top {top} vendedores</h3>
  {_ranking_table(summary.by_seller.head(top), "Vendedor")}
  <h3>Top {top} produtos</h3>
  {_ranking_table(summary.by_product.head(top), "Produto")}
  <p style="color:#666;font-size:12px">O relatório completo está em anexo (Excel).
  E-mail gerado automaticamente.</p>
</body>
</html>"""


def build_message(settings: SmtpSettings, subject: str, html_body: str, attachment: Path) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = settings.sender
    message["To"] = ", ".join(settings.recipients)
    message.set_content("Seu cliente de e-mail não exibe HTML. O relatório completo está em anexo.")
    message.add_alternative(html_body, subtype="html")

    mime_type, _ = mimetypes.guess_type(attachment.name)
    maintype, subtype = (mime_type or "application/octet-stream").split("/", 1)
    message.add_attachment(
        attachment.read_bytes(), maintype=maintype, subtype=subtype, filename=attachment.name
    )
    return message


def send_message(settings: SmtpSettings, message: EmailMessage) -> None:
    context = ssl.create_default_context()
    with smtplib.SMTP(settings.host, settings.port, timeout=30) as smtp:
        smtp.starttls(context=context)
        smtp.login(settings.username, settings.password)
        smtp.send_message(message)


def _ranking_table(table: pd.DataFrame, label_column: str) -> str:
    header = (
        "<tr style='background:#1F4E78;color:#fff'>"
        f"<th style='padding:6px 12px;text-align:left'>{label_column}</th>"
        "<th style='padding:6px 12px'>Faturamento</th>"
        "<th style='padding:6px 12px'>Participação</th></tr>"
    )
    rows = "".join(
        f"<tr><td style='padding:6px 12px'>{html.escape(str(row[label_column]))}</td>"
        f"<td style='padding:6px 12px;text-align:right'>{format_brl(row['Faturamento'])}</td>"
        f"<td style='padding:6px 12px;text-align:right'>{format_percent(row['Participação'])}</td></tr>"
        for _, row in table.iterrows()
    )
    return f"<table style='border-collapse:collapse'>{header}{rows}</table>"
