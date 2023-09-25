#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp solution :
        # dp_max[i] refers to the max value end with i
        # dp_min[i] refers to the min value end with i
        # time complexity: O(n)
        # space complexity: O(1)

        dpMin = dpMax = maxNum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                dpMax, dpMin = dpMin, dpMax
            dpMax = max(nums[i], nums[i]*dpMax)
            dpMin = min(nums[i], nums[i]*dpMin)
            maxNum = max(maxNum, dpMax)
        return maxNum
# @lc code=end
