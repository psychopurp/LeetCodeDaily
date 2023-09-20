#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Bottom-up DP approach
        # time complexity: O(N)
        # space complexity: O(N*5)
        """
        For each day, we are one of the following 5 states:
        1.No operation
        2.First time to buy stock
        3.First time to sell stock
        4.Second time to buy stock
        5.Second time to sell stock

        state1 = max(last state1, last state 0 - prices[i])
        state2 = max(last state2, last state 1 + prices[i])
        state3 and state4 same as above

        explanation: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.md
        """
        pass

        n = len(prices)
        dp = [[0 for _ in range(5)] for _ in range(n)]

        # initial state
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]  # buy and sell at the first day then buy the second time
        dp[0][4] = 0

        for i in range(1, n):
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])

        return dp[-1][-1]


# @lc code=end
