#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # time complexity: O(logN)
        # space complexity: O(1)

        left, right = 0, len(nums)-1
        while left < right:
            mid = (left+right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
# @lc code=end
