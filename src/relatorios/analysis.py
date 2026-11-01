"""Cálculo dos indicadores do relatório."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

import pandas as pd


@dataclass(frozen=True)
class SalesSummary:
    period_start: date
    period_end: date
    total_revenue: float
    total_sales: int
    total_items: int
    average_ticket: float
    by_month: pd.DataFrame
    by_seller: pd.DataFrame
    by_product: pd.DataFrame
    by_region: pd.DataFrame


def summarize(sales: pd.DataFrame, top_products: int = 10) -> SalesSummary:
    """Consolida as vendas em indicadores gerais e rankings por mês, vendedor, produto e região."""
    if sales.empty:
        raise ValueError("Não há vendas para resumir.")

    total_revenue = float(sales["faturamento"].sum())
    total_sales = len(sales)

    return SalesSummary(
        period_start=sales["data"].min().date(),
        period_end=sales["data"].max().date(),
        total_revenue=total_revenue,
        total_sales=total_sales,
        total_items=int(sales["quantidade"].sum()),
        average_ticket=total_revenue / total_sales,
        by_month=_by_month(sales),
        by_seller=_ranking(sales, "vendedor", "Vendedor", total_revenue),
        by_product=_ranking(sales, "produto", "Produto", total_revenue).head(top_products),
        by_region=_ranking(sales, "regiao", "Região", total_revenue),
    )


def filter_month(sales: pd.DataFrame, month: str) -> pd.DataFrame:
    """Mantém só as vendas do mês informado no formato ``AAAA-MM``."""
    period = pd.Period(month, freq="M")
    return sales[sales["data"].dt.to_period("M") == period].reset_index(drop=True)


def _aggregate(grouped) -> pd.DataFrame:
    return grouped.agg(
        Vendas=("faturamento", "size"),
        Itens=("quantidade", "sum"),
        Faturamento=("faturamento", "sum"),
    )


def _ranking(sales: pd.DataFrame, column: str, label: str, total_revenue: float) -> pd.DataFrame:
    table = _aggregate(sales.groupby(column)).sort_values("Faturamento", ascending=False)
    table["Participação"] = table["Faturamento"] / total_revenue
    return table.rename_axis(label).reset_index()


def _by_month(sales: pd.DataFrame) -> pd.DataFrame:
    table = _aggregate(sales.groupby(sales["data"].dt.to_period("M"))).sort_index()
    table["Variação"] = table["Faturamento"].pct_change()
    table.index = table.index.astype(str)
    return table.rename_axis("Mês").reset_index()
