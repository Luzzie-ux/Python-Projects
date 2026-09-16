def string_sculptor(text: str) -> str:
    if not text:
        return ""
    swicth: bool = False
    l: list[str] = []
    for c in text:
        if not swicth and c != ' ':
            l.append(c.lower())
            swicth = True
        if swicth and c  == ' ':
            l.append(c.upper())
            swicth = False
    return "".join(l)
