from unittest.mock import MagicMock, patch

import pytest
from openpyxl import load_workbook

from relatorios.analysis import summarize
from relatorios.cli import main
from relatorios.email_report import (
    EmailConfigError,
    SmtpSettings,
    build_html_summary,
    build_message,
    load_env_file,
    send_message,
)
from relatorios.excel_report import CURRENCY_FORMAT, write_excel_report

SMTP_ENV = {
    "SMTP_HOST": "smtp.exemplo.com",
    "SMTP_USUARIO": "robo@exemplo.com",
    "SMTP_SENHA": "segredo",
    "RELATORIO_DESTINATARIOS": "gestor@exemplo.com, financeiro@exemplo.com",
}


def test_excel_report_has_all_sheets_formats_and_chart(sales, tmp_path):
    path = write_excel_report(summarize(sales), sales, tmp_path / "rel.xlsx")

    workbook = load_workbook(path)
    assert workbook.sheetnames == ["Resumo", "Mensal", "Vendedores", "Produtos", "Regiões", "Dados"]
    assert workbook["Vendedores"]["A2"].value == "Ana"
    assert workbook["Vendedores"]["D2"].number_format == CURRENCY_FORMAT
    assert workbook["Resumo"]["B3"].number_format == CURRENCY_FORMAT
    assert len(workbook["Mensal"]._charts) == 1


def test_html_summary_contains_kpis_and_escapes_names(sales):
    sales.loc[0, "vendedor"] = "<script>"
    html_body = build_html_summary(summarize(sales))

    assert "R$ 2.100,00" in html_body
    assert "&lt;script&gt;" in html_body
    assert "<script>" not in html_body


def test_smtp_settings_from_env():
    settings = SmtpSettings.from_env(SMTP_ENV)

    assert settings.port == 587
    assert settings.sender == "robo@exemplo.com"
    assert settings.recipients == ["gestor@exemplo.com", "financeiro@exemplo.com"]


def test_smtp_settings_reports_missing_variables():
    with pytest.raises(EmailConfigError, match="SMTP_SENHA"):
        SmtpSettings.from_env({k: v for k, v in SMTP_ENV.items() if k != "SMTP_SENHA"})


def test_load_env_file_does_not_override_existing_values(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("# comentário\nSMTP_HOST=do-arquivo\nSMTP_PORTA='2525'\n", encoding="utf-8")
    env = {"SMTP_HOST": "ja-definido"}

    load_env_file(env_file, env)

    assert env == {"SMTP_HOST": "ja-definido", "SMTP_PORTA": "2525"}


def test_message_has_html_and_attachment(tmp_path):
    attachment = tmp_path / "rel.xlsx"
    attachment.write_bytes(b"conteudo")
    settings = SmtpSettings.from_env(SMTP_ENV)

    message = build_message(settings, "Assunto", "<p>oi</p>", attachment)

    assert message["To"] == "gestor@exemplo.com, financeiro@exemplo.com"
    attachments = list(message.iter_attachments())
    assert [a.get_filename() for a in attachments] == ["rel.xlsx"]


def test_send_message_uses_tls_and_login(tmp_path):
    attachment = tmp_path / "rel.xlsx"
    attachment.write_bytes(b"x")
    settings = SmtpSettings.from_env(SMTP_ENV)
    message = build_message(settings, "Assunto", "<p>oi</p>", attachment)

    with patch("relatorios.email_report.smtplib.SMTP") as smtp_class:
        smtp = MagicMock()
        smtp_class.return_value.__enter__.return_value = smtp
        send_message(settings, message)

    smtp.starttls.assert_called_once()
    smtp.login.assert_called_once_with("robo@exemplo.com", "segredo")
    smtp.send_message.assert_called_once_with(message)


def test_cli_generates_excel_and_html(sales_dir, tmp_path):
    output = tmp_path / "saida"

    exit_code = main(["--entrada", str(sales_dir), "--saida", str(output), "--mes", "2026-10"])

    assert exit_code == 0
    assert (output / "relatorio_vendas_2026-10.xlsx").is_file()
    assert (output / "relatorio_vendas_2026-10.html").is_file()


@pytest.mark.parametrize("month", ["2026-13", "outubro", "2020-01"])
def test_cli_rejects_invalid_or_empty_month(sales_dir, tmp_path, month):
    assert main(["--entrada", str(sales_dir), "--saida", str(tmp_path), "--mes", month]) == 1


def test_cli_fails_without_smtp_configuration(sales_dir, tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    for name in SMTP_ENV:
        monkeypatch.delenv(name, raising=False)

    assert main(["--entrada", str(sales_dir), "--saida", str(tmp_path), "--enviar-email"]) == 1
