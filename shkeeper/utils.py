from decimal import Decimal


def format_decimal(d: Decimal, precision: int = 8) -> str:
    f = str(round(d.normalize(), precision))
    return f.rstrip('0').rstrip('.') if '.' in f else f
