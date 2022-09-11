#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start
from typing import List


class Solution:
    # def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    #     # Top-down DP : dp[i] refers to whether s[i:] can be segmented into wordDict
    #     # time complexity: O(M^2*N) M=len(s) N=len(wordDict)
    #     # space complexity: O(M)
    #     def dp(i: int) -> bool:
    #         if i == len(s):
    #             return True

    #         if i in memo:
    #             return memo[i]

    #         # O(N)
    #         for word in wordDict:
    #             n = len(word)  # O(M)
    #             if s[i:i+n] == word and dp(i+n):
    #                 memo[i] = True
    #                 return True
    #         memo[i] = False
    #         return False

    #     memo = {}
    #     return dp(0)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom-up DP : dp[i] refers to whether s[i:] can be segmented into wordDict
        # time complexity: O(M^2*N) M=len(s) N=len(wordDict)
        # space complexity: O(M)

        n = len(s)
        dp = [False]*(n+1)
        dp[-1] = True

        for i in range(n-1, -1, -1):

            for word in wordDict:
                m = len(word)
                if dp[i+1] and s[i-m+1:i+1] == word:
                    dp[i-m+1] = True

        return dp[0]


# @lc code=end
