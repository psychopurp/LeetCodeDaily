#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start


class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # 动态规划 时间复杂度O(n*k) 空间复杂度O(n)
    #     # dp返回数值为n 是所需要的最少硬币数
    #     def dp(n):
    #         if n == 0:
    #             return 0
    #         if n < 0:
    #             return -1
    #         if dp_table[n - 1] != 0:
    #             return dp_table[n-1]
    #         res = float('inf')
    #         for i in coins:
    #             sub = dp(n - i)
    #             if sub == -1:
    #                 continue
    #             res = min(res, sub + 1)
    #         dp_table[n-1] = res if res != float('inf') else -1
    #         return dp_table[n-1]

    #     dp_table = [0]*amount
    #     return dp(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        # 动态规划 时间复杂度O(n*k) 空间复杂度O(n)
        # dp[n]=min(dp[amount-coin]...)+1

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if coin > i:
                    continue
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1
        # @lc code=end
