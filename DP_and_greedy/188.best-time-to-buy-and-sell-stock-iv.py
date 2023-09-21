#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#

# @lc code=start
from typing import List


class Solution:
    # def maxProfit(self, k: int, prices: List[int]) -> int:
    #     # Bottom-up DP approach with 2D array
    #     # time complexity: O(N)
    #     # space complexity: O(N*K*2)
    #     """
    #     For each day, we are one of the following states:
    #     1.No operation
    #     2.First time to buy stock
    #     3.First time to sell stock
    #     4.Second time to buy stock
    #     5.Second time to sell stock
    #     ... Kth time to buy stock
    #     ... Kth time to sell stock

    #     state1 = max(last state1, last state 0 - prices[i])
    #     state2 = max(last state2, last state 1 + prices[i])
    #     state3 and state4 same as above

    #     explanation: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.md
    #     """

    #     n = len(prices)
    #     dp = [[0 for _ in range(2 * k + 1)] for _ in range(n)]

    #     # initial state
    #     for j in range(1, 2 * k + 1, 2):
    #         dp[0][j] = -prices[0]

    #     for i in range(1, n):
    #         for j in range(1, 2 * k + 1):
    #             if j % 2 == 0:
    #                 # state sell
    #                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
    #             else:
    #                 # state buy
    #                 dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])

    #     return dp[-1][-1]

    def maxProfit(self, k: int, prices: List[int]) -> int:
        # Bottom-up DP approach with 3D array
        # time complexity: O(N)
        # space complexity: O(N*K*2)
        """
        For each day, we are one of the following states:
        1.No operation
        2.First time to buy stock
        3.First time to sell stock
        4.Second time to buy stock
        5.Second time to sell stock
        ... Kth time to buy stock
        ... Kth time to sell stock

        state1 = max(last state1, last state 0 - prices[i])
        state2 = max(last state2, last state 1 + prices[i])
        state3 and state4 same as above

        explanation: https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0123.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAIII.md
        """

        n = len(prices)
        # [day][transaction][buy or sell]
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]

        # initial state
        for j in range(1, k + 1):
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])

        return dp[-1][-1][0]


# @lc code=end
