import random
from typing import List

"""
Selection Sort

Time complexity: 
- Worst:O(N^2)
- Best:O(N^2)
Space complexity: O(1)

Stablity: not stable
"""


def generate_random_list(length: int, min_value: int, max_value: int) -> List[int]:
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list


def selection_sort(nums: List[int]):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        nums[i], nums[min_idx] = nums[min_idx], nums[i]


if __name__ == "__main__":
    nums = generate_random_list(10, 0, 100)
    selection_sort(nums)
    print(nums == sorted(nums))
