def pattern_tracker(text: str) -> int:
    count: int = 0
    n: int = len(text)
    ni: int
    nj: int
    for i in range(1, n):
        try:
            ni = int(text[i])
            nj = int(text[i - 1])
        except ValueError:
            continue
        if ni > nj:
            count +=1
    return count
