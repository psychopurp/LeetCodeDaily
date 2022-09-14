#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
from functools import lru_cache


class Solution:
    # def minDistance(self, word1: str, word2: str) -> int:
    #     # Top-down dp
    #     # time complexity: O(3^min(m,n)) n=len(word1) m=len(word2) optimized to O(m*n) by using cache.
    #     # space complexity: O(max(m,n))

    #     @lru_cache(None)
    #     def dp(s1: str, s2: str) -> int:
    #         if not s1 or not s2:
    #             return max(len(s1), len(s2))

    #         if s1[-1] == s2[-1]:
    #             return dp(s1[:-1], s2[:-1])

    #         insert = dp(s1, s2[:-1])
    #         delete = dp(s1[:-1], s2)
    #         replace = dp(s1[:-1], s2[:-1])
    #         return min(insert, delete, replace)+1

    #     return dp(word1, word2)

    # def minDistance(self, word1: str, word2: str) -> int:
    #     # Bottom-up dp
    #     # time complexity: O(m*n) n=len(word1) m=len(word2) optimized to O(m*n) by using cache.
    #     # space complexity: O(m*n) can be optimized to O(min(m,n)) by using just one row of DP array

    #     m, n = len(word1), len(word2)
    #     dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

    #     for i in range(1, n+1):
    #         dp[i][0] = dp[i-1][0]+1

    #     for j in range(1, m+1):
    #         dp[0][j] = dp[0][j-1]+1

    #     for i in range(1, n+1):
    #         for j in range(1, m+1):
    #             if word2[i-1] == word1[j-1]:
    #                 dp[i][j] = dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1

    #     return dp[-1][-1]

    def minDistance(self, word1: str, word2: str) -> int:
        # Top-down dp
        # time complexity: O(3^min(m,n)) n=len(word1) m=len(word2) optimized to O(m*n) by using cache.
        # space complexity: O(max(m,n))

        @lru_cache(None)
        def dp(i: int, j: int):

            if i < 0 or j < 0:
                return max(i, j)+1

            if word1[i] == word2[j]:
                return dp(i-1, j-1)

            return min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1))+1

        return dp(len(word1)-1, len(word2)-1)

# @lc code=end
