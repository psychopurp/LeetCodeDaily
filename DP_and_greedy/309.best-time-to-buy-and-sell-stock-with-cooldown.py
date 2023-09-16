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

        for i in range(n):
            if i == 0:
                dp[i][1] = -prices[i]
                continue
            if i == 1:
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
                dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])
                continue

            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
            dp[i][0] = max(dp[i - 1][1] + prices[i], dp[i - 1][0])

        return dp[n - 1][0]


# @lc code=end
