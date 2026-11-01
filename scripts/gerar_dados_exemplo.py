"""Gera planilhas de vendas fictícias em dados/exemplo para demonstrar a automação.

Os arquivos imitam exportações reais: um CSV com vírgula, outro com ponto e vírgula
e valores no formato brasileiro, e algumas linhas "sujas" (vazias, negativas,
duplicadas) que o processo de limpeza deve descartar.

Uso: python scripts/gerar_dados_exemplo.py
"""

from __future__ import annotations

import csv
import random
from datetime import date, timedelta
from pathlib import Path

OUTPUT_DIR = Path(__file__).resolve().parent.parent / "dados" / "exemplo"

SELLERS = ["Ana Lima", "Bruno Costa", "Carla Mendes", "Diego Rocha", "Elisa Prado", "Felipe Nunes"]
REGIONS = ["Sudeste", "Sul", "Nordeste", "Centro-Oeste", "Norte"]
PRODUCTS = {
    "Notebook Pro 14": 5899.00,
    "Monitor 27 4K": 2199.90,
    "Teclado Mecânico": 449.90,
    "Mouse Sem Fio": 129.90,
    "Headset USB": 289.00,
    "Webcam Full HD": 349.00,
    "SSD 1TB": 499.90,
    "Hub USB-C": 219.90,
    "Cadeira Ergonômica": 1599.00,
    "Suporte para Notebook": 159.90,
    "Impressora Laser": 1299.00,
    "Roteador Wi-Fi 6": 699.00,
}
HEADER = ["Data", "Vendedor", "Produto", "Região", "Quantidade", "Valor Unitário"]


def random_rows(rng: random.Random, month_start: date, count: int) -> list[list[str]]:
    rows = []
    for _ in range(count):
        product = rng.choice(list(PRODUCTS))
        day = month_start + timedelta(days=rng.randrange(28))
        price = PRODUCTS[product] * rng.choice([1, 1, 1, 0.95, 0.9])  # alguns descontos
        rows.append(
            [
                day.isoformat(),
                rng.choice(SELLERS),
                product,
                rng.choice(REGIONS),
                str(rng.choices([1, 2, 3, 5, 10], weights=[50, 25, 12, 8, 5])[0]),
                f"{price:.2f}",
            ]
        )
    return rows


def to_brazilian(rows: list[list[str]]) -> list[list[str]]:
    """Data como DD/MM/AAAA e valores como 1.234,56, como exporta o Excel em português."""
    converted = []
    for day, seller, product, region, quantity, price in rows:
        y, m, d = day.split("-")
        value = f"{float(price):,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
        converted.append([f"{d}/{m}/{y}", seller, product, region, quantity, value])
    return converted


def write_csv(path: Path, rows: list[list[str]], delimiter: str) -> None:
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerow(HEADER)
        writer.writerows(rows)


def main() -> None:
    rng = random.Random(42)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    august = random_rows(rng, date(2026, 8, 1), 180)
    september = random_rows(rng, date(2026, 9, 1), 210)
    october = random_rows(rng, date(2026, 10, 1), 240)

    # Linhas problemáticas que a limpeza deve rejeitar ou remover.
    october += [
        october[0],  # duplicada
        ["2026-10-12", "", "Mouse Sem Fio", "Sul", "1", "129.90"],  # sem vendedor
        ["2026-10-13", "Ana Lima", "SSD 1TB", "Sudeste", "-2", "499.90"],  # quantidade negativa
        ["data-invalida", "Bruno Costa", "Hub USB-C", "Norte", "1", "219.90"],  # data inválida
    ]

    write_csv(OUTPUT_DIR / "vendas_2026-08.csv", august, ",")
    write_csv(OUTPUT_DIR / "vendas_2026-09.csv", to_brazilian(september), ";")
    write_csv(OUTPUT_DIR / "vendas_2026-10.csv", october, ",")
    print(f"Arquivos gerados em {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
