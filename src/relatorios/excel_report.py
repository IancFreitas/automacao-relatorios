"""Geração do relatório em Excel, com abas formatadas e gráfico."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font, PatternFill
from openpyxl.worksheet.worksheet import Worksheet

from relatorios.analysis import SalesSummary

CURRENCY_FORMAT = '"R$" #,##0.00'
PERCENT_FORMAT = "0.0%"
DATE_FORMAT = "DD/MM/YYYY"

CURRENCY_HEADERS = {"Faturamento", "Valor unitário"}
PERCENT_HEADERS = {"Participação", "Variação"}
DATE_HEADERS = {"Data"}

HEADER_FONT = Font(bold=True, color="FFFFFF")
HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
MAX_COLUMN_WIDTH = 45

DATA_COLUMNS = {
    "data": "Data",
    "vendedor": "Vendedor",
    "produto": "Produto",
    "regiao": "Região",
    "quantidade": "Quantidade",
    "valor_unitario": "Valor unitário",
    "faturamento": "Faturamento",
    "arquivo_origem": "Arquivo de origem",
}


def write_excel_report(summary: SalesSummary, sales: pd.DataFrame, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        _kpi_table(summary).to_excel(writer, sheet_name="Resumo", index=False)
        summary.by_month.to_excel(writer, sheet_name="Mensal", index=False)
        summary.by_seller.to_excel(writer, sheet_name="Vendedores", index=False)
        summary.by_product.to_excel(writer, sheet_name="Produtos", index=False)
        summary.by_region.to_excel(writer, sheet_name="Regiões", index=False)
        sales[list(DATA_COLUMNS)].rename(columns=DATA_COLUMNS).to_excel(
            writer, sheet_name="Dados", index=False
        )

        for sheet in writer.sheets.values():
            _format_sheet(sheet)

        _format_kpis(writer.sheets["Resumo"])
        _add_monthly_chart(writer.sheets["Mensal"])

    return path


def _kpi_table(summary: SalesSummary) -> pd.DataFrame:
    period = f"{summary.period_start:%d/%m/%Y} a {summary.period_end:%d/%m/%Y}"
    return pd.DataFrame(
        [
            ("Período", period),
            ("Faturamento total", summary.total_revenue),
            ("Número de vendas", summary.total_sales),
            ("Itens vendidos", summary.total_items),
            ("Ticket médio", summary.average_ticket),
            ("Vendedor com maior faturamento", summary.by_seller.iloc[0]["Vendedor"]),
            ("Produto com maior faturamento", summary.by_product.iloc[0]["Produto"]),
        ],
        columns=["Indicador", "Valor"],
    )


def _format_sheet(sheet: Worksheet) -> None:
    headers = [cell.value for cell in sheet[1]]
    for cell in sheet[1]:
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL

    for index, header in enumerate(headers, start=1):
        number_format = (
            CURRENCY_FORMAT if header in CURRENCY_HEADERS
            else PERCENT_FORMAT if header in PERCENT_HEADERS
            else DATE_FORMAT if header in DATE_HEADERS
            else None
        )
        column = sheet.cell(row=1, column=index).column_letter
        width = len(str(header))
        for cell in sheet[column][1:]:
            if number_format:
                cell.number_format = number_format
            width = max(width, len(str(cell.value)) if cell.value is not None else 0)
        sheet.column_dimensions[column].width = min(width + 3, MAX_COLUMN_WIDTH)

    sheet.freeze_panes = "A2"


def _format_kpis(sheet: Worksheet) -> None:
    for row in sheet.iter_rows(min_row=2):
        label, value = row
        if label.value in {"Faturamento total", "Ticket médio"}:
            value.number_format = CURRENCY_FORMAT
        elif isinstance(value.value, int):
            value.number_format = "#,##0"
    sheet.column_dimensions["B"].width = 28


def _add_monthly_chart(sheet: Worksheet) -> None:
    headers = [cell.value for cell in sheet[1]]
    revenue_column = headers.index("Faturamento") + 1
    last_row = sheet.max_row

    chart = BarChart()
    chart.title = "Faturamento por mês"
    chart.y_axis.title = "R$"
    chart.legend = None
    chart.add_data(
        Reference(sheet, min_col=revenue_column, min_row=1, max_row=last_row), titles_from_data=True
    )
    chart.set_categories(Reference(sheet, min_col=1, min_row=2, max_row=last_row))
    chart.width, chart.height = 18, 9
    sheet.add_chart(chart, f"{sheet.cell(row=1, column=len(headers) + 2).column_letter}2")
