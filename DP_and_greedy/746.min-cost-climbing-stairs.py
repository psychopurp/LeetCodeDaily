#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start
from typing import List


class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     # 1. DFS solution: will MLE!
    #     # time complexity: O(2^N)
    #     # space complexity: O(log N)
    #     n = len(cost)

    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dfs(i: int, pay: int) -> int:
    #         if i >= n:
    #             return pay

    #         # 1.one step
    #         one_step = dfs(i + 1, pay + cost[i])
    #         # 2.two step
    #         two_step = dfs(i + 2, pay + cost[i])

    #         return min(one_step, two_step)

    #     return min(dfs(0, 0), dfs(1, 0))

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     # 2.Top-down DP
    #     # time complexity: O(N)
    #     # space complexity: O(N)
    #     n = len(cost)

    #     """
    #     dp[i] = min(dp[i-1],dp[i-2])+cost[i]
    #     """

    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int) -> int:
    #         if i < 0:
    #             return 0

    #         return min(dp(i - 1), dp(i - 2)) + cost[i]

    #     cost.append(0)
    #     n = len(cost)
    #     return dp(n - 1)

    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     # 3.Bottom-up DP
    #     # time complexity: O(N)
    #     # space complexity: O(N)
    #     n = len(cost)

    #     """
    #     dp[i] = min(dp[i-1],dp[i-2])+cost[i]
    #     """

    #     from functools import lru_cache

    #     cost.append(0)
    #     n = len(cost)
    #     dp = [cost[i] for i in range(n)]

    #     for i in range(2, n):
    #         dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

    #     return dp[n - 1]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 4.Top-down DP solution 2
        # time complexity: O(N)
        # space complexity: O(1)
        n = len(cost)

        """
        dp[i] = min(dp[i-1]+cost[i-1] , dp[i-2]+cost[i-2])

        dp[0]=dp[1]=0
        The dp array represents the minimum amount required to climb the corresponding steps
        """
        from functools import lru_cache

        @lru_cache(None)
        def dp(i: int) -> int:
            if i <= 1:
                return 0

            return min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])

        n = len(cost)
        return dp(n)


# @lc code=end
