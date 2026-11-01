import pandas as pd
import pytest

from relatorios.loader import DataError, load_sales, normalize_column, parse_dates, parse_number


def test_load_sales_cleans_and_consolidates_files(sales_dir):
    result = load_sales(sales_dir)

    assert len(result.files) == 2
    assert result.rejected_rows == 2
    assert result.duplicated_rows == 1
    assert len(result.sales) == 3
    assert result.sales["faturamento"].sum() == pytest.approx(200 + 300 + 1500)


def test_load_sales_sorts_by_date(sales_dir):
    sales = load_sales(sales_dir).sales

    assert sales["data"].is_monotonic_increasing
    assert sales.iloc[0]["data"] == pd.Timestamp("2026-09-15")


def test_load_sales_reads_excel_files(tmp_path):
    pd.DataFrame(
        {
            "Data": ["2026-10-01"],
            "Vendedor": ["Ana"],
            "Produto": ["Mouse"],
            "Região": ["Sul"],
            "Quantidade": [3],
            "Valor Unitário": [50],
        }
    ).to_excel(tmp_path / "vendas.xlsx", index=False)

    sales = load_sales(tmp_path).sales

    assert sales.iloc[0]["faturamento"] == 150


def test_missing_columns_raise_data_error(tmp_path):
    (tmp_path / "ruim.csv").write_text("Data,Vendedor\n2026-10-01,Ana\n", encoding="utf-8")

    with pytest.raises(DataError, match="colunas obrigatórias ausentes"):
        load_sales(tmp_path)


def test_empty_folder_raises_data_error(tmp_path):
    with pytest.raises(DataError, match="Nenhum arquivo"):
        load_sales(tmp_path)


def test_missing_folder_raises_data_error(tmp_path):
    with pytest.raises(DataError, match="não encontrada"):
        load_sales(tmp_path / "nao-existe")


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("Região", "regiao"), (" Valor Unitário ", "valor_unitario"), ("QUANTIDADE", "quantidade")],
)
def test_normalize_column(raw, expected):
    assert normalize_column(raw) == expected


def test_parse_number_handles_brazilian_and_international_formats():
    parsed = parse_number(pd.Series(["1.234,56", "1234.56", "R$ 10,00", "abc", None]))

    assert parsed.iloc[0] == pytest.approx(1234.56)
    assert parsed.iloc[1] == pytest.approx(1234.56)
    assert parsed.iloc[2] == pytest.approx(10.0)
    assert parsed.iloc[3:].isna().all()


def test_parse_dates_never_swaps_day_and_month():
    parsed = parse_dates(pd.Series(["2026-08-04", "04/08/2026", "2026-08-04 00:00:00", "31/02/2026", "x"]))

    assert parsed.iloc[0] == pd.Timestamp("2026-08-04")
    assert parsed.iloc[1] == pd.Timestamp("2026-08-04")
    assert parsed.iloc[2] == pd.Timestamp("2026-08-04")
    assert parsed.iloc[3:].isna().all()
