def compare(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return len(s1) > len(s2)
    return s1.lower() > s2.lower()


def cryptic_sorter(strings: list[str]) -> list[str]:
    n: int = len(strings)
    if n == 0 or not strings[0]:
        return strings
    for i in range(n):
        for j in range(i + 1, n):
            if compare(strings[i], strings[j]):
                strings[i], strings[j] = strings[j], strings[i]
    return strings

l = cryptic_sorter(strings=["apple","cat","banana","dog","elephant"])
print(l)
l = cryptic_sorter(strings=["aaa","bbb","AAA","BBB"])
print(l)
l = cryptic_sorter(strings=["hello","hey","hi","test"])
print(l)
l = cryptic_sorter(strings=[])
print(l)
l = cryptic_sorter(strings=[""])
print(l)
