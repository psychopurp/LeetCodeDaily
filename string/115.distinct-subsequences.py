#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] Distinct Subsequences
#


# @lc code=start
class Solution:
    # def numDistinct(self, s: str, t: str) -> int:
    #     # Top-down DP solution
    #     # time complexity: O(M*N) M=len(s) N=len(t)
    #     # space complexity: O(M*N) stack usage
    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int, j: int) -> int:
    #         if j == 0:
    #             return 1

    #         if i == 0:
    #             return 0

    #         if s[i - 1] == t[j - 1]:
    #             return dp(i - 1, j - 1) + dp(i - 1, j)
    #         else:
    #             return dp(i - 1, j)

    #     return dp(len(s), len(t))

    def numDistinct(self, s: str, t: str) -> int:
        # Bottom-up DP solution
        # time complexity: O(M*N) M=len(s) N=len(t)
        # space complexity: O(M*N)

        """
        dp[i][j] represents count of subsequences of s[:i] and t[:j]
        """

        m, n = len(s), len(t)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # init base case
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    # delete one char from s
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


# @lc code=end
