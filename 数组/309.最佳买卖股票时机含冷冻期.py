#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
        # 时间复杂度O(N) 空间复杂度O(1)
        if not prices:
            return 0
        dp_i_0, dp_i_1, dp_pre_0 = 0, -prices[0], 0
        for i in range(1, len(prices)):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, dp_pre_0-prices[i])
            dp_pre_0 = tmp
        return dp_i_0

        # @lc code=end
