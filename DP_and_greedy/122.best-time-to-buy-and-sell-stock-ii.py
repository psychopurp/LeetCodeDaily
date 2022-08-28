#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     # greedy algorithm
    #     # time complexity: O(N)
    #     # space complexity: O(1)
    #     profit = 0
    #     for i in range(1, len(prices)):
    #         if prices[i] > prices[i-1]:
    #             profit += prices[i] - prices[i-1]

    #     return profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     # Monotonous stack
    #     # time complexity: O(N)
    #     # space complexity: O(1)
    #     '''
    #     https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/208241/Explanation-for-the-dummy-like-me

    #     main idea: find the smallest day to buy, and then biggest day to sell.
    #     example: [3, 2, 5, 8, 1, 9]

    #     the buying day is monotonous from high price to lower price
    #     the selling day in monotonous from lower price to higher price

    #     1. buy: 2 sell: 8
    #     2. buy: 1 sell: 9
    #     the range [3, 2, 5, 8, 1, 9] will be splitted into 2 sub-ranges [3, 2, 5, 8] and [1, 9].
    #     '''

    #     buy = sell = profit = 0
    #     i = 0
    #     while i < len(prices)-1:

    #         while i < len(prices)-1 and prices[i+1] <= prices[i]:
    #             i += 1
    #         buy = prices[i]

    #         while i < len(prices)-1 and prices[i+1] >= prices[i]:
    #             i += 1
    #         sell = prices[i]

    #         profit += sell-buy
    #     return profit

    def maxProfit(self, prices: List[int]) -> int:
        # DP
        # time complexity: O(N)
        # space complexity: O(1)
        '''
        For every day, we've three choices:
        1.Don't do anything
        2.Sell them for a profit
        3.Buy new stock
        '''

        curHold, curNotHold = float("-inf"), 0
        for price in prices:
            prevHold, prevNotHold = curHold, curNotHold

            # either keep hold, or buy in stock today at stock price
            curHold = max(prevHold, prevNotHold-price)

            # either keep not-hold, or sell out stock today at stock price
            curNotHold = max(prevNotHold, prevHold+price)

        # maximum profit must be in not-hold state
        return curNotHold

# @lc code=end
