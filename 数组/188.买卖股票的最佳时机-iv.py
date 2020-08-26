#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # dp[3][2][1] 代表第三天第二笔交易手上有股票
        # 时间复杂度O(M*N) 空间复杂度O(N)
        if not prices:
            return 0

        if k >= len(prices)//2:  # 退化为不限制交易次数
            # k设为无穷大
            dp_i_0, dp_i_1 = 0, -prices[0]
            for i in range(1, len(prices)):
                tmp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
                dp_i_1 = max(dp_i_1, tmp-prices[i])
            return dp_i_0

        dp = [[0, 0] for j in range(k+1)]
        for i in range(len(prices)):
            for j in range(1, k+1):
                if i == 0:
                    dp[j][0] = 0
                    dp[j][1] = -prices[i]
                    continue
                dp[j][0] = max(dp[j][0], dp[j][1]+prices[i])
                dp[j][1] = max(dp[j][1], dp[j-1][0]-prices[i])
        return dp[-1][0]

    # @lc code=end
