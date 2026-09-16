def scarecrow_whisper(order: str, shift: int) -> str:
    s = ""
    base: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    low: str = base.lower()
    for c in order:
        if c in low and 'a' <= c <= 'z':
            pos = (low.index(c) + shift) % 26
            s += low[(pos)]
        elif c in base and 'A' <= c <= 'Z':
            pos = (base.index(c) + shift) % 26
            s += base[pos]
        else:
            s += c
    return s
