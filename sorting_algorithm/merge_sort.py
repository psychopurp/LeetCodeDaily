import random
from typing import List

"""
Merge Sort

Time complexity: 
- Worst:O(N*logN)
- Best:O(N*logN)
Space complexity: O(N)

Stablity: stable
"""


def generate_random_list(length: int, min_value: int, max_value: int) -> List[int]:
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list


def merge_sort(nums: List[int]):
    def merge(left: List[int], right: List[int]) -> List[int]:
        # time complexity: O(N)
        res = []
        i = j = 0
        while i < len(left) or j < len(right):
            if i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1
                else:
                    res.append(right[j])
                    j += 1
                continue

            if i < len(left):
                res.append(left[i])
                i += 1
                continue

            if j < len(right):
                res.append(right[j])
                j += 1

        return res

    def sort(l: int, r: int) -> List[int]:
        # time complexity: O(N)
        if l == r:
            return [nums[l]]
        # devide
        mid = (l + r) >> 1
        # left part
        left_half = sort(l, mid)
        # right part
        right_half = sort(mid + 1, r)

        return merge(left_half, right_half)

    return sort(0, len(nums) - 1)


if __name__ == "__main__":
    nums = generate_random_list(4, 0, 10)
    print(nums)
    nums = merge_sort(nums)
    print(nums)
    print(nums == sorted(nums))
