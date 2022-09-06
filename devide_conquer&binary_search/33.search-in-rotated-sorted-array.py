#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search
        # time complexity: O(log N)
        # space complexity: O(1)
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            # left side is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            # right side is sorted
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
# @lc code=end
