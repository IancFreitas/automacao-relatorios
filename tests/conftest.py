from pathlib import Path

import pandas as pd
import pytest

HEADER = "Data,Vendedor,Produto,Região,Quantidade,Valor Unitário\n"


@pytest.fixture
def sales_dir(tmp_path: Path) -> Path:
    """Pasta com dois arquivos pequenos: um CSV padrão e um no formato brasileiro."""
    (tmp_path / "outubro.csv").write_text(
        HEADER
        + "2026-10-01,Ana,Mouse,Sul,2,100.00\n"
        + "2026-10-02,Bruno,Teclado,Norte,1,300.00\n"
        + "2026-10-02,Bruno,Teclado,Norte,1,300.00\n"  # duplicada
        + "2026-10-03,,Mouse,Sul,1,100.00\n"  # sem vendedor
        + "2026-10-04,Ana,Mouse,Sul,0,100.00\n",  # quantidade zero
        encoding="utf-8",
    )
    (tmp_path / "setembro.csv").write_text(
        HEADER.replace(",", ";") + "15/09/2026;Ana;Monitor;Sul;1;1.500,00\n",
        encoding="utf-8",
    )
    return tmp_path


@pytest.fixture
def sales() -> pd.DataFrame:
    frame = pd.DataFrame(
        {
            "data": pd.to_datetime(["2026-09-10", "2026-10-01", "2026-10-02", "2026-10-03"]),
            "vendedor": ["Ana", "Ana", "Bruno", "Bruno"],
            "produto": ["Monitor", "Mouse", "Teclado", "Mouse"],
            "regiao": ["Sul", "Sul", "Norte", "Norte"],
            "quantidade": [1, 2, 1, 1],
            "valor_unitario": [1500.0, 100.0, 300.0, 100.0],
            "arquivo_origem": ["a.csv"] * 4,
        }
    )
    frame["faturamento"] = frame["quantidade"] * frame["valor_unitario"]
    return frame
