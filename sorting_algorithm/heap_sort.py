import random
from typing import List

"""
Heap Sort

Time complexity: 
- Worst:O(N*logN)
- Best:O(N*logN)
Space complexity: O(1)

Stablity: Not stable
"""


def generate_random_list(length: int, min_value: int, max_value: int) -> List[int]:
    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list


def heap_sort(nums: List[int]):
    import heapq

    heap = []

    for i in range(len(nums)):
        heapq.heappush(heap, nums[i])

    for i in range(len(nums)):
        nums[i] = heapq.heappop(heap)


if __name__ == "__main__":
    nums = generate_random_list(4, 0, 10)
    nums = [5, 1, 1, 2, 0, 0]
    print(nums)
    heap_sort(nums)
    print(nums)
    print(nums == sorted(nums))
