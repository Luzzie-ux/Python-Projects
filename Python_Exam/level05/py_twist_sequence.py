def twist_sequence(arr: list[int], k: int) -> list[int]:
    if not arr or not k:
        return arr
    while k > 0:
        arr.insert(0, arr.pop())
        k -= 1
    return arr
