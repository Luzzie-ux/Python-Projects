def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    l: list[int] = list1 + list2
    n: int = len(l)
    for i in range(n):
        for j in range(i + 1, n):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l
