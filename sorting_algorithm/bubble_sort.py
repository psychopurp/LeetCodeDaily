import random
from typing import List


def generate_random_list(length: int, min_value: int, max_value: int) -> List[int]:
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list


def bubble_sort(nums: List[int]):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]


if __name__ == "__main__":
    nums = generate_random_list(10, 0, 100)
    bubble_sort(nums)
    print(nums == sorted(nums))
