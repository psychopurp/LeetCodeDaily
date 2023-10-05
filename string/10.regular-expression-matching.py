#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] Regular Expression Matching
#


# @lc code=start


class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    #     # 1. DP solution
    #     # time complexity: O(M*N) M=len(s) N=len(P)
    #     # space complexity: O(M*N) stack size

    #     from functools import lru_cache

    #     @lru_cache
    #     def is_match(s: str, p: str) -> bool:
    #         if p == "":
    #             return s == ""

    #         first_match = s != "" and (s[0] == p[0] or p[0] == ".")

    #         if len(p) >= 2 and p[1] == "*":
    #             return is_match(s, p[2:]) or (first_match and is_match(s[1:], p))

    #         return first_match and is_match(s[1:], p[1:])

    #     return is_match(s, p)

    # def isMatch(self, s: str, p: str) -> bool:
    #     # 2. DP solution
    #     # time complexity: O(M*N) M=len(s) N=len(P)
    #     # space complexity: O(M*N) stack size

    #     from functools import lru_cache

    #     @lru_cache
    #     def dp(i: int, j: int) -> bool:
    #         if j == len(p):
    #             return i == len(s)

    #         first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")

    #         if j + 1 < len(p) and p[j + 1] == "*":
    #             return dp(i, j + 2) or (first_match and dp(i + 1, j))

    #         return first_match and dp(i + 1, j + 1)

    #     return dp(0, 0)

    def isMatch(self, s: str, p: str) -> bool:
        # 3. Bottom-up DP
        # time complexity: O(M*N) M=len(s) N=len(P)
        # space complexity: O(M*N)

        """
        dp[i][j] represents s[:i+1] to p[j+1] whether matched
        if p[j-1]=="*":
            dp[i][j]=dp[i]j-2] || (dp[i-1][j] && p[j-2]==".") || (dp[i-1][j] && p[j-2]==s[i-1])
        else:
            dp[i][j]=dp[i-1][j-1] && (p[j-1]=="." || p[j-1]==s[i-1])
        """

        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        # initialization
        dp[0][0] = True  # two empty string

        # bad case
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                # s is empty but p can be empty because of *
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    # dp[i][j-2] : * repeat 0 time
                    # dp[i-1][j] : * repeat 1 or more times
                    if p[j - 2] == s[i - 1] or p[j - 2] == ".":
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (
                        p[j - 1] == "." or p[j - 1] == s[i - 1]
                    )
        return dp[-1][-1]


# @lc code=end
