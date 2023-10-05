#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     # 1.From middle to two ends
    #     # time complexity: O(N^2)
    #     # space complexity: O(1)

    #     # get the longest palindrome, l, r are the middle indexes
    #     # from inner to outer
    #     def expandAroundCenter(l: int, r: int):
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             l -= 1
    #             r += 1
    #         return l + 1, r - 1

    #     start = end = 0
    #     for i in range(len(s)):
    #         # odd case like "aba"
    #         l1, r1 = expandAroundCenter(i, i)
    #         # even case like "abba"
    #         l2, r2 = expandAroundCenter(i, i + 1)
    #         if r1 - l1 > end - start:
    #             start, end = l1, r1
    #         if r2 - l2 > end - start:
    #             start, end = l2, r2
    #     return s[start : end + 1]

    # def longestPalindrome(self, s: str) -> str:
    #     # 2.DP correct but TLE
    #     # time complexity: O(N^2)
    #     # space complexity: O(1)

    #     from functools import lru_cache

    #     n = len(s)
    #     res = ""

    #     @lru_cache
    #     def dp(i: int, j: int) -> bool:
    #         if j == i:
    #             return True
    #         if j - i == 1:
    #             return s[i] == s[j]

    #         return s[i] == s[j] and dp(i + 1, j - 1)

    #     for i in range(n):
    #         for j in range(i, n):
    #             if dp(i, j):
    #                 if j - i + 1 > len(res):
    #                     res = s[i : j + 1]

    #     return res

    def longestPalindrome(self, s: str) -> str:
        # 3.Bottom-up DP : dp(i,j) represents from i to j whether a palindrome
        # dp(i,j)= dp(i+1,j-1) & s[i]==s[j]
        # time complexity: O(N^2)
        # space complexity: O(N^2)

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        max_start = 0  # start position
        max_end = 0  # end position

        for r in range(1, n):
            for l in range(0, r):
                dp[l][r] = s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1])
                if dp[l][r] and r - l > max_end - max_start:
                    max_start, max_end = l, r

        return s[max_start : max_end + 1]


# @lc code=end
