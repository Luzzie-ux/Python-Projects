def bracket_validator(s: str) -> bool:
    pairs: dict[str, str] = {'(':')', '[':']','{':'}',}
    open: list[str] = []
    for char in s:
        if char in pairs:
            open.append(char)
        elif char in pairs.values():
            if not len(open) or pairs[open[-1]] != char:
                return False
            open.pop()
    return len(open) == 0
