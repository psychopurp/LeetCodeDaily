#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start


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

    def maxProfit(self, prices: List[int]) -> int:
        # 单调栈
        if not prices:
            return 0
        profit = 0
        stack = []
        for i in prices:
            if not stack:
                stack.append(i)
                continue
            if i < stack[-1]:
                stack[-1] = i
                continue
            if i > stack[-1]:
                profit = max(profit, i - stack[-1])
        return profit


# @lc code=end
