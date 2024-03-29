#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     # 1.Brute force solution: whis will MLE
    #     # time complexity: O(N^2)
    #     # space complexity: O(N^2)
    #     n = len(nums) + 1

    #     dp = [[0 for _ in range(n)] for _ in range(n)]
    #     max_val = float("-inf")

    #     for i in range(1, n):
    #         dp[i][i] = nums[i - 1]

    #     for i in range(1, n):
    #         for j in range(i, n):
    #             dp[i][j] = dp[i][j - 1] + nums[j - 1]
    #             max_val = max(max_val, dp[i][j])

    #     return max_val

    # def maxSubArray(self, nums: List[int]) -> int:
    #     # 2.DP optimization from brute force
    #     # time complexity: O(N)
    #     # space complexity: O(N)
    #     n = len(nums) + 1

    #     dp = [0 for _ in range(n)]
    #     max_val = float("-inf")

    #     for i in range(1, n):
    #         dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])
    #         max_val = max(max_val, dp[i])

    #     return max_val

    # def maxSubArray(self, nums: List[int]) -> int:
    #     # Bottom-up DP :
    #     # time complexity: O(N)
    #     # space complexity: O(1)
    #     '''
    #     Use dp[i] to represent the maximum sum of a continuous subarray
    #     ending with index i
    #     '''
    #     max_num = float("-inf")
    #     for i in range(len(nums)):
    #         if i > 0:
    #             nums[i] = max(nums[i], nums[i-1]+nums[i])
    #         max_num = max(max_num, nums[i])
    #     return max_num

    def maxSubArray(self, nums: List[int]) -> int:
        # Top-down DP : dp[i] represents largest sum till i
        # time complexity: O(N)
        # space complexity: O(N) stack usage

        def dp(i: int):
            nonlocal max_val
            val = 0
            if i == 0:
                val = nums[i]
            else:
                val = max(nums[i], dp(i - 1) + nums[i])
            max_val = max(max_val, val)
            return val

        max_val = float("-inf")
        dp(len(nums) - 1)
        return max_val


# @lc code=end
