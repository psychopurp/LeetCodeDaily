#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start


class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     # 利用最小堆实现
    #     # 时间复杂度: O(N logk)。
    #     # 空间复杂度: O(k)，用于存储堆元素
    #     import heapq
    #     heap = nums[:k]
    #     heapq.heapify(heap)
    #     for i in nums[k:]:
    #         if i > heap[0]:
    #             heapq.heapreplace(heap, i)
    #     return heap[0]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 利用快排思想实现
        # 时间复杂度: O(N)。
        # 空间复杂度: O(1)，原地排序
        def partition(left, right):
            '''切分'''
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] >= pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[left] = pivot
            return left

        n = len(nums)
        target = n - k
        left = 0
        right = n - 1
        while True:
            base = partition(left, right)
            if base == target:
                return nums[base]
            elif target > base:
                left = base + 1
            else:
                righ = base-1


# @lc code=end
