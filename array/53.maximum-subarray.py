#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     # brute force solution
    #     # time complexity: O(n^2)
    #     # space complexity: O(1)
    #     maxNum = nums[0]
    #     n = len(nums)
    #     for i in range(n):
    #         tmp = 0
    #         for j in range(i, n):
    #             tmp += nums[j]
    #             maxNum = max(tmp, maxNum)
    #     return maxNum

    # def maxSubArray(self, nums: List[int]) -> int:
    #     # DP solution: dp[i] equals to largest sum ends with i
    #     # time complexity: O(n)
    #     # space complexity: O(n)
    #     dp = [nums[0]]
    #     maxNum = nums[0]

    #     for i in range(1, len(nums)):
    #         dp.append(max(nums[i], dp[-1]+nums[i]))
    #         if dp[-1] > maxNum:
    #             maxNum = dp[-1]

    #     return maxNum

    def maxSubArray(self, nums: List[int]) -> int:
        # DP solution: optimize space complexity
        # time complexity: O(n)
        # space complexity: O(1)
        dp = nums[0]
        maxNum = nums[0]
        for i in range(1, len(nums)):
            dp = max(nums[i], dp+nums[i])
            if dp > maxNum:
                maxNum = dp
        return maxNum
# @lc code=end
