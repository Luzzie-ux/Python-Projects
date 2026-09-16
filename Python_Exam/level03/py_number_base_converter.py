def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if any(not(2 <= b <= 36) for b in (from_base, to_base)):
        return "ERROR"
    decimal: int
    base: str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    try:
        decimal = int(number, from_base)
    except ValueError:
        return "ERROR"
    if not decimal:
        return "0"
    l: list[str] = []
    while decimal > 0:
        l.append(base[decimal % to_base])
        decimal //= to_base
    return "".join(reversed(l))
