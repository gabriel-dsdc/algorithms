from typing import List, Literal


def find_duplicate(lst: List[int]) -> int | Literal[False]:
    if any(type(x) != int or x < 1 for x in lst):
        return False

    lst.sort()
    start, end = 0, len(lst) - 1

    while len(lst) > 1:
        mid = (start + end) // 2
        first_half = lst[start : mid + 1]
        second_half = lst[mid + 1 : end + 1]

        if first_half[-1] == second_half[0]:
            return first_half[-1]

        if len(set(first_half)) < len(first_half):
            end = mid
            continue

        if len(set(second_half)) < len(second_half):
            start = mid + 1
            continue
        return False
    return False
