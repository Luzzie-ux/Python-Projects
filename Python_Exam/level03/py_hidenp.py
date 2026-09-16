def hidenp(small: str, big: str) -> bool:
    if not small:
        return True
    it = iter(big)
    return all(c in it for c in small)
