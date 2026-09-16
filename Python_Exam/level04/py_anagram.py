def anagram(s1: str, s2: str) -> bool:
    s1, s2 = s1.replace(' ', ''), s2.replace(' ', '')
    s1, s2 = s1.lower(), s2.lower()
    if not s1 or not s2:
        return True
    elif len(s1) != len(s2):
        return False
    l1, l2 = list(s1), list(s2)
    l1.sort(), l2.sort()
    return l1 == l2
