#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] Wildcard Matching
#


# @lc code=start
class Solution:
    # def isMatch(self, s: str, p: str) -> bool:
    #     # 1.DP solution: scan from left to right
    #     # time complexity: O(M*N) M=len(s) N=len(p)
    #     # space complexity: O(M*N) stack usage

    #     from functools import lru_cache

    #     @lru_cache
    #     def is_match(s: str, p: str) -> bool:
    #         if not p:
    #             return not s

    #         if not s:
    #             return p[0] == "*" and is_match(s, p[1:])

    #         if p[0] == "?":
    #             return is_match(s[1:], p[1:])

    #         if p[0] == "*":
    #             return is_match(s[1:], p) or is_match(s, p[1:])

    #         return s[0] == p[0] and is_match(s[1:], p[1:])

    #     return is_match(s, p)

    # def isMatch(self, s: str, p: str) -> bool:
    #     # 2.DP solution: scan from left to right with optimization(without str slices)
    #     # time complexity: O(M*N) M=len(s) N=len(p)
    #     # space complexity: O(M*N) stack usage

    #     from functools import lru_cache

    #     @lru_cache
    #     def is_match(i: int, j: int) -> bool:
    #         if j == len(p):
    #             return i == len(s)

    #         if i == len(s):
    #             return p[j] == "*" and is_match(i, j + 1)

    #         if p[j] == "?":
    #             return is_match(i + 1, j + 1)

    #         if p[j] == "*":
    #             return is_match(i + 1, j) or is_match(i, j + 1)

    #         return s[i] == p[j] and is_match(i + 1, j + 1)

    #     return is_match(0, 0)

    # def isMatch(self, s: str, p: str) -> bool:
    #     # 3.DP solution: scan from right to left
    #     # time complexity: O(M*N) M=len(s) N=len(p)
    #     # space complexity: O(M*N) stack usage

    #     from functools import lru_cache

    #     @lru_cache
    #     def is_match(i: int, j: int) -> bool:
    #         if j == 0:
    #             return i == 0

    #         if i == 0:
    #             return p[j - 1] == "*" and is_match(i, j - 1)

    #         if p[j - 1] == "*":
    #             return is_match(i - 1, j) or is_match(i, j - 1)

    #         if p[j - 1] == "?":
    #             return is_match(i - 1, j - 1)

    #         return s[i - 1] == p[j - 1] and is_match(i - 1, j - 1)

    #     return is_match(len(s), len(p))

    def isMatch(self, s: str, p: str) -> bool:
        # 4.Bottom-up DP solution: scan from right to left
        # time complexity: O(M*N) M=len(s) N=len(p)
        # space complexity: O(M*N) stack usage

        m, n = len(s), len(p)
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]

        # initialize base case
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                    continue

                dp[i][j] = (p[j - 1] == "?" or p[j - 1] == s[i - 1]) and dp[i - 1][
                    j - 1
                ]
        return dp[-1][-1]


# @lc code=end
