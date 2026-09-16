def echo_validator(text: str) -> bool:
    if not text:
        return False
    l = [c.lower() for c in text if c != ' ']
    return l == l[::-1]
