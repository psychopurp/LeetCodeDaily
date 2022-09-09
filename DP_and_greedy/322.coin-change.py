#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List


class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     # Top-down DP : dp[i] represent minimum coin comination for the amount
    #     # time complexity: O(M*N) M=amount N=len(coins)
    #     # space complexity: O(M)
    #     def dp(n: int) -> int:
    #         if n == 0:
    #             return 0
    #         if n < 0:
    #             return -1

    #         if n in memo:
    #             return memo[n]

    #         min_num = float('inf')
    #         for coin in coins:
    #             sub = dp(n-coin)
    #             if sub == -1:
    #                 continue
    #             min_num = min(sub+1, min_num)

    #         memo[n] = min_num if min_num != float('inf')else -1
    #         return memo[n]
    #     memo = {}
    #     return dp(amount)

    def coinChange(self, coins: List[int], amount: int) -> int:
        # Bottom-up DP : dp[i] represent minimum coin comination for the amount
        # time complexity: O(M*N) M=amount N=len(coins)
        # space complexity: O(M)

        dp = [0]*(amount+1)

        for i in range(1, amount+1):
            count = []
            for coin in coins:
                if i == coin:
                    count.append(0)
                elif i > coin:
                    if dp[i-coin] != -1:
                        count.append(dp[i-coin])

            dp[i] = min(count)+1 if count else -1
        return dp[-1]

# @lc code=end
