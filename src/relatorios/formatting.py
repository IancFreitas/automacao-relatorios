"""Formatação de valores no padrão brasileiro."""


def format_brl(value: float) -> str:
    """``1234.5`` -> ``"R$ 1.234,50"``."""
    formatted = f"{value:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
    return f"R$ {formatted}"


def format_percent(value: float) -> str:
    """``0.1234`` -> ``"12,3%"``."""
    return f"{value * 100:.1f}%".replace(".", ",")
