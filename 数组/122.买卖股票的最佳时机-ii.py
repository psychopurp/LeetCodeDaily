#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     money=0
    #     for i,k in enumerate(prices):
    #         if i+1==len(prices):
    #             break
    #         if prices[i+1]>prices[i]:
    #             money=money-prices[i]+prices[i+1]

    #     return money

    # def maxProfit(self, prices: List[int]) -> int:
    #     # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-l-3/
    #     # 0代表没股票，1代表有股票
    #     dp = [[0, 1] for i in range(len(prices))]
    #     for i in range(len(prices)):
    #         if i == 0:
    #             dp[i][0] = 0
    #             dp[i][1] = -prices[i]
    #             continue
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
    #         dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
    #     return dp[-1][0]

    def maxProfit(self, prices: List[int]) -> int:
        # 上面的空间优化写法
        if not prices:
            return 0
        dp_i_0, dp_i_1 = 0, -prices[0]
        for i in range(1, len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, tmp-prices[i])
        return dp_i_0

# @lc code=end
