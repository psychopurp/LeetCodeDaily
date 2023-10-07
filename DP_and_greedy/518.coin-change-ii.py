#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] Coin Change II
#

# @lc code=start
from typing import List


class Solution:
    # def change(self, amount: int, coins: List[int]) -> int:
    #     # 1. two-dimensions array DP
    #     # time complexity: O(M*N) M=amount N=len(coins)
    #     # space complexity: O(M*N)

    #     """
    #     i=count of the coins
    #     j=amount
    #     dp[i][j]=dp[i-1][j] + dp[i][j-coins[i-1]]

    #     1.not using the ith coin, only using the first i-1 coins to make up amount j, then we have dp[i-1][j] ways.
    #     2.using the ith coin, since we can use unlimited same coin, we need to know how many ways to make up amount j - coins[i-1] by using first i coins(including ith), which is dp[i][j-coins[i-1]]
    #     Initialization: dp[i][0] = 1

    #     link: https://leetcode.com/problems/coin-change-ii/solutions/99212/knapsack-problem-java-solution-with-thinking-process-o-nm-time-and-o-m-space/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
    #     """

    #     m = len(coins)

    #     dp = [[0 for _ in range(amount + 1)] for _ in range(m + 1)]

    #     for i in range(m + 1):
    #         dp[i][0] = 1

    #     for i in range(1, m + 1):
    #         for j in range(1, amount + 1):
    #             if j >= coins[i - 1]:
    #                 dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
    #             else:
    #                 dp[i][j] = dp[i - 1][j]

    #     return dp[-1][-1]

    def change(self, amount: int, coins: List[int]) -> int:
        # 2. one-dimension array DP: optimization of previous solution
        # time complexity: O(M*N) M=amount N=len(coins)
        # space complexity: O(M)

        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j >= coins[i]:
                    dp[j] = dp[j] + dp[j - coins[i]]
        return dp[-1]


# @lc code=end
