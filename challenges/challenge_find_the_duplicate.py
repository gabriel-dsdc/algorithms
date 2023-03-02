from typing import Literal


def binary_search(lst: list, target) -> int:
    start = 0
    end = len(lst) - 1

    while start <= end:
        mid = (start + end) // 2

        if lst[mid] == target:
            return mid

        if target < lst[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


def find_duplicate(nums: list[int]) -> int | Literal[False]:
    nums.sort()
    end = len(nums) - 1
    for num in nums:
        if type(num) != int or num < 1:
            return False

        num_index = binary_search(nums, num)
        if num_index < end:
            if num == nums[num_index + 1] or num == nums[num_index - 1]:
                return num
    return False
