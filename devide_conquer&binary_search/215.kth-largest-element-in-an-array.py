#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
from typing import List


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # using heap
    #     # time complexity: O(N*log(N))
    #     # space complexity: O(N)

    #     import heapq

    #     heapq.heapify(nums)
    #     for _ in range(len(nums)-k):
    #         heapq.heappop(nums)

    #     return heapq.heappop(nums)

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # using heap, optimized
    #     # time complexity: O(N*log(K))
    #     # space complexity: O(K)

    #     import heapq

    #     heap = nums[:k]
    #     heapq.heapify(heap)

    #     for i in range(k, len(nums)):
    #         x = nums[i]
    #         if x > heap[0]:
    #             heapq.heapreplace(heap, x)
    #     return heap[0]

    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # using Quick Select
    #     # time complexity: O(N)
    #     # space complexity: O(1)

    #     def partition_from_left(nums: List[int], l: int, r: int) -> int:
    #         pivot = l
    #         while r > l:
    #             # find the one which smaller than base from the right
    #             while r > l and nums[r] >= nums[pivot]:
    #                 r -= 1

    #             # find the one which greater than base from the left
    #             while r > l and nums[l] <= nums[pivot]:
    #                 l += 1

    #             # swap
    #             nums[l], nums[r] = nums[r], nums[l]

    #         # swap the pivot
    #         nums[l], nums[pivot] = nums[pivot], nums[l]
    #         return l

    #     def partition_from_right(nums: List[int], l: int, r: int) -> int:
    #         pivot = r
    #         while l < r:
    #             # find the one which greater than base from the left
    #             while l < r and nums[l] <= nums[pivot]:
    #                 l += 1

    #             # find the one which smaller than base from the right
    #             while l < r and nums[r] >= nums[pivot]:
    #                 r -= 1

    #             # swap
    #             nums[l], nums[r] = nums[r], nums[l]

    #         # swap the pivot
    #         nums[r], nums[pivot] = nums[pivot], nums[r]
    #         return r

    #     l, r = 0, len(nums)-1
    #     target = len(nums)-k
    #     while l <= r:

    #         pivot = partition_from_right(nums, l, r)
    #         if pivot == target:
    #             return nums[pivot]
    #         if pivot > target:
    #             r = pivot-1
    #         else:
    #             l = pivot+1

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using Quick Select
        # time complexity: O(N)
        # space complexity: O(logN)

        if not nums:
            return

        pivot = nums[-1]

        mid = []
        left, right = [], []
        for x in nums:
            if x > pivot:
                left.append(x)
            elif x < pivot:
                right.append(x)
            else:
                mid.append(x)

        L, M = len(left), len(mid)
        if k <= L:
            return self.findKthLargest(left, k)
        elif k > L+M:
            return self.findKthLargest(right, k-L-M)
        else:
            return mid[0]


# @lc code=end
