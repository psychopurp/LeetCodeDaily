#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int], fee: int) -> int:

    #     dp = [[0, 0] for i in prices]
    #     dp[0][0] = 0
    #     dp[0][1] = -(fee+prices[0])
    #     for i in range(1, len(prices)):
    #         dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
    #         dp[i][1] = max(dp[i-1][1], dp[i-1][0]-fee-prices[i])
    #     return dp[-1][0]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 上面算法的空间复杂度优化方法 O(1) 时间复杂度O(N)
        dp_i_0, dp_i_1 = 0, -fee-prices[0]
        for i in range(1, len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0-fee-prices[i])
        return dp_i_0
        # @lc code=end
