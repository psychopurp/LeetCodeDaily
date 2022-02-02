#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(1)

        x = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[x] = nums[i]
                x += 1

        return x
# @lc code=end
