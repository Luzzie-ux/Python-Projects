def string_permutation_checker(s1: str, s2: str) -> bool:
    l1, l2 = list(s1), list(s2)
    l1.sort(), l2.sort()
    return l1 == l2
