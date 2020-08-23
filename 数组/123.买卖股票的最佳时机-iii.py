#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     # dp[3][2][1] 的含义就是：今天是第三天，我现在手上持有着股票，至今最多进行 2 次交易
    #     k = 2
    #     dp = [[[0, 0] for j in range(k)] for i in prices]
    #     for i in range(len(prices)):
    #         if i == 0:
    #             dp[i][0][0] = 0
    #             dp[i][0][1] = -prices[i]
    #             dp[i][1][0] = 0
    #             dp[i][1][1] = -prices[i]
    #             continue
    #         dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1]+prices[i])
    #         dp[i][0][1] = max(dp[i-1][0][1], -prices[i]) #第一次交易，且有股票
    #         dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i])
    #         dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i])
    #     return dp[-1][1][0]

    def maxProfit(self, prices: List[int]) -> int:
        # 上面解法的空间优化
        dp_0_0, dp_1_0 = 0, 0
        dp_0_1, dp_1_1 = -prices[0], -prices[0]
        for i in range(1, len(prices)):
            dp_0_0 = max(dp_0_0, dp_0_1+prices[i])
            dp_0_1 = max(dp_0_1, -prices[i])
            dp_1_0 = max(dp_1_0, dp_1_1+prices[i])
            dp_1_1 = max(dp_1_1, dp_0_0-prices[i])
        return dp_1_0

# @lc code=end
