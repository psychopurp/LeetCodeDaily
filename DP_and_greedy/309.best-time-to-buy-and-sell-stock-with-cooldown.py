#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Bottom-up DP
        # time complexity: O(N)
        # space complexity: O(N)
        """
        For every day, we've three choices:
        1.Don't do anything
        2.Sell them for a profit
        3.Buy new stock
        dp[i][0] represents on day i, we don't have stock, which means we either sold it or kept last state
        dp[i][1] represents on day i, we have stock, which means we either bought it or kept last state
        """
        n = len(prices)
        dp = [[0, 0] for _ in range(n)]

        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            if i == 1:
                dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
            else:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])

        return dp[-1][0]

    # def maxProfit(self, prices: List[int]) -> int:
    #     # Bottom-up DP with state machine thinking
    #     # time complexity: O(N)
    #     # space complexity: O(N)
    #     """
    #     There are 4 states we may be in for each day:
    #     1.Holding stock
    #     Not Holding:
    #         2.Keep last not holding state
    #         3.Sell today
    #     4.Colldown
    #     """

    #     n = len(prices)
    #     dp = [[0, 0, 0, 0] for _ in range(n)]

    #     # initialize state
    #     dp[0][0] = -prices[0]

    #     for i in range(1, n):
    #         dp[i][0] = max(
    #             dp[i - 1][0], dp[i - 1][3] - prices[i], dp[i - 1][1] - prices[i]
    #         )
    #         dp[i][1] = max(dp[i - 1][1], dp[i - 1][3])
    #         # if we want to sell today we must have stock yesterday
    #         dp[i][2] = dp[i - 1][0] + prices[i]
    #         dp[i][3] = dp[i - 1][2]

    #     return max(dp[-1])


# @lc code=end
