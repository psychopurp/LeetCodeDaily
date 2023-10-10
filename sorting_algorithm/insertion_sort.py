import random
from typing import List

"""
Insertion Sort

Time complexity: 
- Worst:O(N^2)
- Best:O(N)
Space complexity: O(1)

Stablity: stable
"""


def generate_random_list(length: int, min_value: int, max_value: int) -> List[int]:
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list


def insertion_sort(nums: List[int]):
    n = len(nums)
    for i in range(1, n):
        cur_value = nums[i]
        j = i - 1

        while j >= 0 and nums[j] > cur_value:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = cur_value


if __name__ == "__main__":
    nums = generate_random_list(4, 0, 10)
    print(nums)
    insertion_sort(nums)
    print(nums)
    print(nums == sorted(nums))
