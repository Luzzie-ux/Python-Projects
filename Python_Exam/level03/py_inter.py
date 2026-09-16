def inter(s1: str, s2: str) -> str:
    l1 = [c for c in s1 if c in s2]
    return "".join(list(dict.fromkeys(l1)))
