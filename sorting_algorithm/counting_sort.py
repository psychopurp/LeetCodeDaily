import random
from typing import List

"""
Counting Sort

Time complexity: 
- Worst:O(N+K)  where K is the range of input which 0<=K<N
- Best:O(N+K)
Space complexity: O(K)


Stablity: stable
"""


def generate_random_list(length: int, min_value: int, max_value: int) -> List[int]:
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list


def counting_sort(nums: List[int]):
    max_val = max(nums)
    bucket = [0 for _ in range(max_val + 1)]

    for i in range(len(nums)):
        bucket[nums[i]] += 1

    x = 0
    for i in range(len(bucket)):
        while bucket[i] > 0:
            nums[x] = i
            x += 1
            bucket[i] -= 1


if __name__ == "__main__":
    nums = generate_random_list(10, 0, 100)
    print(nums)
    counting_sort(nums)
    print(nums)
    print(nums == sorted(nums))
