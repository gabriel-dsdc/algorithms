def merge_sort(lst: list, start=0, end=None):
    if end is None:
        end = len(lst)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(lst, start, mid)
        merge_sort(lst, mid, end)
        merge(lst, start, mid, end)


def merge(lst: list, start, mid, end):
    left = lst[start:mid]
    right = lst[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            lst[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            lst[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            lst[general_index] = left[left_index]
            left_index += 1
        else:
            lst[general_index] = right[right_index]
            right_index += 1


def is_anagram(first_string: str, second_string: str) -> tuple[str, str, bool]:
    first_str = list(first_string.lower())
    second_str = list(second_string.lower())

    merge_sort(first_str)
    merge_sort(second_str)

    first_str = "".join(first_str)
    second_str = "".join(second_str)

    return (
        first_str,
        second_str,
        first_str == second_str if first_str else False,
    )
