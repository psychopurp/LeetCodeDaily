#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
from typing import List


class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     # Bottom-up DP
    #     # time complexity: O(N)
    #     # space complexity: O(N) can be optimized to O(1) by using variable instead of DP array.
    #     '''
    #     dp[i] represent the maximum amount till i.
    #     dp[i] = max( dp[i-1] , dp[i-2]+nums[i])
    #     dp[i-2]+nums[i] : we rob the i
    #     dp[i-1] : we did't rob the i
    #     '''
    #     if len(nums) == 1:
    #         return nums[0]

    #     n = len(nums)
    #     dp1 = [0]*(n+2)
    #     dp2 = [0]*(n+2)

    #     for i in range(len(nums)):
    #         if i > 0:
    #             dp1[i] = max(dp1[i-2]+nums[i], dp1[i-1])

    #         if i < n-1:
    #             dp2[i] = max(dp2[i-2]+nums[i], dp2[i-1])

    #     return max(max(dp1), max(dp2))

    def rob(self, nums: List[int]) -> int:
        # Bottom-up DP
        # time complexity: O(N)
        # space complexity: O(1)
        '''
        rob : represents the maximum amount we will have if last night we robbed
        not_rob : represents the amount we will have if last night we did't rob
        '''

        if len(nums) == 1:
            return nums[0]

        def simple_rob(i: int, j: int) -> int:
            rob = not_rob = 0
            for k in range(i, j):
                rob, not_rob = not_rob+nums[k], max(rob, not_rob)
            return max(rob, not_rob)

        return max(simple_rob(1, len(nums)), simple_rob(0, len(nums)-1))


# @lc code=end
