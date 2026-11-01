from datetime import date

import pandas as pd
import pytest

from relatorios.analysis import filter_month, summarize
from relatorios.formatting import format_brl, format_percent


def test_summarize_computes_kpis(sales):
    summary = summarize(sales)

    assert summary.total_revenue == pytest.approx(2100)
    assert summary.total_sales == 4
    assert summary.total_items == 5
    assert summary.average_ticket == pytest.approx(525)
    assert summary.period_start == date(2026, 9, 10)
    assert summary.period_end == date(2026, 10, 3)


def test_rankings_are_sorted_by_revenue_with_share(sales):
    summary = summarize(sales)

    assert list(summary.by_seller["Vendedor"]) == ["Ana", "Bruno"]
    assert summary.by_seller["Faturamento"].tolist() == pytest.approx([1700, 400])
    assert summary.by_seller["Participação"].sum() == pytest.approx(1)
    assert summary.by_product.iloc[0]["Produto"] == "Monitor"


def test_top_products_limits_ranking(sales):
    assert len(summarize(sales, top_products=2).by_product) == 2


def test_by_month_is_chronological_with_variation(sales):
    by_month = summarize(sales).by_month

    assert list(by_month["Mês"]) == ["2026-09", "2026-10"]
    assert pd.isna(by_month.iloc[0]["Variação"])
    assert by_month.iloc[1]["Variação"] == pytest.approx(600 / 1500 - 1)


def test_filter_month(sales):
    october = filter_month(sales, "2026-10")

    assert len(october) == 3
    assert (october["data"].dt.month == 10).all()


def test_summarize_rejects_empty_data(sales):
    with pytest.raises(ValueError):
        summarize(sales.iloc[0:0])


@pytest.mark.parametrize(
    ("value", "expected"),
    [(1234.5, "R$ 1.234,50"), (0, "R$ 0,00"), (1_000_000, "R$ 1.000.000,00")],
)
def test_format_brl(value, expected):
    assert format_brl(value) == expected


def test_format_percent():
    assert format_percent(0.1234) == "12,3%"
