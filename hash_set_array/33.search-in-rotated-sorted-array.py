#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start

from typing import List


class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     if not nums:
    #         return - 1
    #     n = len(nums)

    #     # 找出旋转的点
    #     def findMin():
    #         begin = 0
    #         end = n - 1
    #         if nums[begin] <= nums[end]:
    #             return 0
    #         while begin < end:
    #             if end - begin == 1:
    #                 return end
    #             mid = (begin + end) // 2
    #             if nums[mid] < nums[begin]:
    #                 end = mid
    #                 continue
    #             if nums[mid] > nums[end]:
    #                 begin = mid
    #                 continue

    #     def binarySearch(begin, end):
    #         if begin >= end:
    #             if target == nums[begin]:
    #                 return begin
    #             else:
    #                 return -1
    #         mid = (begin + end) // 2
    #         if target <= nums[mid]:
    #             return binarySearch(begin, mid)
    #         else:
    #             return binarySearch(mid+1, end)

    #     min_index = findMin()
    #     if min_index == 0:
    #         if nums[0] <= target <= nums[n-1]:
    #             return binarySearch(0, n - 1)
    #         else:
    #             return -1
    #     elif nums[0] <= target <= nums[min_index - 1]:
    #         return binarySearch(0, min_index - 1)
    #     elif nums[min_index] <= target <= nums[len(nums) - 1]:
    #         return binarySearch(min_index, len(nums)-1)
    #     else:
    #         return -1

    # def search(self, nums: List[int], target: int) -> int:
    #     if not nums:
    #         return - 1
    #     left, right = 0, len(nums) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if nums[mid] == target:
    #             return mid
    #         # 说明左边连续递增
    #         if nums[left] <= nums[mid]:
    #             if nums[left] <= target <= nums[mid]:
    #                 right = mid - 1  # [left,mid)
    #             else:
    #                 left = mid + 1  # (mid,right]
    #         else:
    #             # 右边连续递增
    #             if nums[mid] <= target <= nums[right]:
    #                 left = mid + 1
    #             else:
    #                 right = mid - 1
    #     return -1

    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # time complexity: O(logN)
        # space complexity: O(1)

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) >> 1
            # rotated part at the right side
            if nums[mid] > nums[right]:
                if target <= nums[right] or target > nums[mid]:
                    left = mid+1
                else:
                    right = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid+1
                else:
                    right = mid

        return right if target == nums[right] else -1
# @lc code=end
