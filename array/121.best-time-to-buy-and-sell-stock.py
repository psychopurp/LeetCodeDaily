#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     if not prices:
    #         return 0
    #     min_val = prices[0]
    #     profit = 0
    #     for i in prices:
    #         if i < min_val:
    #             min_val = i
    #         profit = max(i - min_val, profit)
    #     return profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     # 单调栈
    #     if not prices:
    #         return 0
    #     profit = 0
    #     stack = []
    #     for i in prices:
    #         if not stack:
    #             stack.append(i)
    #             continue
    #         if i < stack[-1]:
    #             stack[-1] = i
    #             continue
    #         if i > stack[-1]:
    #             profit = max(profit, i - stack[-1])
    #     return profit

    # def maxProfit(self, prices: List[int]) -> int:
    #     # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/
    #     # 0代表没股票，1代表有股票
    #     if not prices:
    #         return 0
    #     dp = [[0, 0] for i in range(len(prices))]

    #     for i in range(len(prices)):
    #         if i == 0:
    #             dp[i][0] = 0
    #             dp[i][1] = -prices[i]
    #             continue
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
    #         dp[i][1] = max(dp[i-1][1], -prices[i])
    #     return dp[-1][0]

    # def maxProfit(self, prices: List[int]) -> int:
    #     # 上面👆解法的空间优化版本
    #     if not prices:
    #         return 0
    #     dp_i_0, dp_i_1 = 0, -prices[0]
    #     for i in range(1, len(prices)):
    #         dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
    #         dp_i_1 = max(dp_i_1, -prices[i])
    #     return dp_i_0

    # def maxProfit(self, prices: List[int]) -> int:
    #     # time complexity: O(n)
    #     # spcae complexity: O(n)
    #     # monotonic stack solution
    #     stack = []
    #     profit = 0
    #     for price in prices:
    #         if not stack:
    #             stack.append(price)
    #             continue

    #         if stack[-1] > price:
    #             stack.append(price)
    #         else:
    #             profit = max(price-stack[-1], profit)

    #     return profit

    def maxProfit(self, prices: List[int]) -> int:
        # time complexity: O(n)
        # spcae complexity: O(1)
        # dynamic programming
        lowestPrice = float('inf')
        profit = 0

        for price in prices:
            lowestPrice = min(lowestPrice, price)
            profit = max(profit, price-lowestPrice)

        return profit


# @lc code=end
