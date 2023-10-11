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
    def merge(l1: int, r1: int, l2: int, r2: int) -> List[int]:
        # time complexity: O(N)
        tmp = nums[l1 : r2 + 1]
        x = l1
        l1, r1 = 0, r1 - l1
        l2, r2 = r1 + 1, r2 - x  # the previous l1

        while l1 <= r1 or l2 <= r2:
            if l1 <= r1 and l2 <= r2:
                if tmp[l1] < tmp[l2]:
                    nums[x] = tmp[l1]
                    l1 += 1
                else:
                    nums[x] = tmp[l2]
                    l2 += 1
            elif l1 <= r1:
                nums[x] = tmp[l1]
                l1 += 1
            elif l2 <= r2:
                nums[x] = tmp[l2]
                l2 += 1
            x += 1

    def merge_sort_range(l: int, r: int) -> List[int]:
        # time complexity: O(log N)
        if l == r:
            return [nums[l]]
        # devide
        mid = (l + r) >> 1
        # left part
        merge_sort_range(l, mid)
        # right part
        merge_sort_range(mid + 1, r)
        merge(l, mid, mid + 1, r)

    merge_sort_range(0, len(nums) - 1)


if __name__ == "__main__":
    nums = generate_random_list(4, 0, 10)
    nums = [5, 1, 1, 2, 0, 0]
    print(nums)
    merge_sort(nums)
    print(nums)
    print(nums == sorted(nums))
