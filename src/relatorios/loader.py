"""Leitura, validação e limpeza das planilhas de vendas."""

from __future__ import annotations

import logging
import unicodedata
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = ["data", "vendedor", "produto", "regiao", "quantidade", "valor_unitario"]
TEXT_COLUMNS = ["vendedor", "produto", "regiao"]
SUPPORTED_SUFFIXES = {".csv", ".xlsx", ".xls"}

logger = logging.getLogger(__name__)


class DataError(Exception):
    """Os arquivos de entrada não puderam ser processados."""


@dataclass(frozen=True)
class LoadResult:
    sales: pd.DataFrame
    files: list[Path]
    rejected_rows: int
    duplicated_rows: int


def load_sales(input_dir: Path) -> LoadResult:
    """Lê todos os CSV/Excel da pasta, valida as colunas e devolve só as linhas válidas.

    Linhas com campos vazios, datas inválidas, quantidade <= 0 ou valor negativo são
    descartadas, assim como linhas duplicadas (o mesmo registro exportado duas vezes).
    É adicionada a coluna ``faturamento = quantidade * valor_unitario``.
    """
    if not input_dir.is_dir():
        raise DataError(f"Pasta de entrada não encontrada: {input_dir}")

    files = sorted(
        path
        for path in input_dir.iterdir()
        if path.suffix.lower() in SUPPORTED_SUFFIXES and not path.name.startswith("~$")
    )
    if not files:
        raise DataError(f"Nenhum arquivo .csv ou .xlsx encontrado em {input_dir}")

    raw = pd.concat([_read_file(path) for path in files], ignore_index=True)
    valid, rejected = _clean(raw)

    deduplicated = valid.drop_duplicates(subset=REQUIRED_COLUMNS, ignore_index=True)
    duplicated = len(valid) - len(deduplicated)

    deduplicated["faturamento"] = deduplicated["quantidade"] * deduplicated["valor_unitario"]
    deduplicated = deduplicated.sort_values("data", ignore_index=True)

    logger.info(
        "%d arquivo(s) lidos: %d linhas válidas, %d rejeitadas, %d duplicadas.",
        len(files),
        len(deduplicated),
        rejected,
        duplicated,
    )
    return LoadResult(deduplicated, files, rejected, duplicated)


def normalize_column(name: object) -> str:
    """``"Região "`` -> ``"regiao"``, ``"Valor Unitário"`` -> ``"valor_unitario"``."""
    ascii_name = unicodedata.normalize("NFKD", str(name)).encode("ascii", "ignore").decode()
    return "_".join(ascii_name.strip().lower().split())


def parse_number(series: pd.Series) -> pd.Series:
    """Converte textos como ``"R$ 1.234,56"`` ou ``"1234.56"`` em número (inválidos viram NaN)."""
    text = series.astype("string").str.replace("R$", "", regex=False).str.strip()
    brazilian = text.str.contains(",", regex=False, na=False)
    text = text.where(~brazilian, text.str.replace(".", "", regex=False).str.replace(",", ".", regex=False))
    return pd.to_numeric(text, errors="coerce")


def parse_dates(series: pd.Series) -> pd.Series:
    """Aceita datas ISO (``2026-10-05``) e brasileiras (``05/10/2026``); o resto vira NaT.

    Os dois formatos são testados explicitamente porque deixar o pandas adivinhar
    (``dayfirst=True``) inverte dia e mês das datas ISO.
    """
    text = series.astype("string").str.strip()
    iso = pd.to_datetime(text, errors="coerce", format="ISO8601")
    brazilian = pd.to_datetime(text, errors="coerce", format="%d/%m/%Y")
    return iso.fillna(brazilian)


def _read_file(path: Path) -> pd.DataFrame:
    try:
        if path.suffix.lower() == ".csv":
            # sep=None detecta automaticamente "," ou ";" (comum em exportações do Excel brasileiro).
            frame = pd.read_csv(path, sep=None, engine="python", dtype=str, encoding="utf-8-sig")
        else:
            frame = pd.read_excel(path, dtype=str)
    except Exception as error:  # qualquer falha de leitura vira uma mensagem amigável
        raise DataError(f"Não foi possível ler {path.name}: {error}") from error

    frame.columns = [normalize_column(column) for column in frame.columns]
    missing = [column for column in REQUIRED_COLUMNS if column not in frame.columns]
    if missing:
        raise DataError(f"{path.name}: colunas obrigatórias ausentes: {', '.join(missing)}")

    frame = frame[REQUIRED_COLUMNS].copy()
    frame["arquivo_origem"] = path.name
    return frame


def _clean(raw: pd.DataFrame) -> tuple[pd.DataFrame, int]:
    frame = raw.copy()
    for column in TEXT_COLUMNS:
        frame[column] = frame[column].str.strip().replace("", pd.NA)

    frame["data"] = parse_dates(frame["data"])
    frame["quantidade"] = parse_number(frame["quantidade"])
    frame["valor_unitario"] = parse_number(frame["valor_unitario"])

    valid = (
        frame[REQUIRED_COLUMNS].notna().all(axis=1)
        & (frame["quantidade"] > 0)
        & (frame["valor_unitario"] >= 0)
    )

    rejected = frame[~valid]
    for file_name, count in rejected["arquivo_origem"].value_counts().items():
        logger.warning("%s: %d linha(s) inválida(s) ignorada(s).", file_name, count)

    cleaned = frame[valid].reset_index(drop=True)
    cleaned["quantidade"] = cleaned["quantidade"].astype(int)
    cleaned["valor_unitario"] = cleaned["valor_unitario"].astype(float)
    return cleaned, len(rejected)
