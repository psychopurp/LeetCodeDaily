#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
from functools import lru_cache


class Solution:
    # def numDecodings(self, s: str) -> int:
    #     # Top-down DP : from right to left
    #     # time complexity: O(2^N)
    #     # space complexity: O(N) used for memorization

    #     @lru_cache(None)
    #     def dp(i: int) -> int:
    #         if i == len(s):
    #             return 1

    #         # sub str starting with 0
    #         if s[i] == '0':
    #             return 0

    #         if i < len(s)-1:
    #             if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
    #                 return dp(i+1)+dp(i+2)
    #         return dp(i+1)

    #     return dp(0)

    # def numDecodings(self, s: str) -> int:
    #     # Bottom-up DP : from right to left
    #     # time complexity: O(N)
    #     # space complexity: O(N) can be optimized to O(1)

    #     n = len(s)
    #     dp = [1]*(n+1)

    #     for i in range(n-1, -1, -1):
    #         if s[i] == '0':
    #             dp[i] = 0
    #             continue

    #         if i < n-1:
    #             if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
    #                 dp[i] = dp[i+1]+dp[i+2]
    #                 continue

    #         dp[i] = dp[i+1]
    #     return dp[0]

    # def numDecodings(self, s: str) -> int:
    #     # Bottom-up DP : from right to left
    #     # time complexity: O(N)
    #     # space complexity: O(1)

    #     n = len(s)
    #     p = pp = 1

    #     for i in range(n-1, -1, -1):
    #         if s[i] == '0':
    #             p, pp = 0, p
    #             continue

    #         if i < n-1:
    #             if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
    #                 p, pp = p+pp, p
    #                 continue

    #         p, pp = p, p
    #     return p

    # def numDecodings(self, s: str) -> int:
    #     # Bottom-up DP : from left to right
    #     # time complexity: O(N)
    #     # space complexity: O(N) can be optimized to O(1)

    #     if s[0] == "0":
    #         return 0

    #     n = len(s)
    #     dp = [1]*(n+1)

    #     for i in range(1, n):

    #         if s[i] == '0':
    #             if s[i-1] == '1' or s[i-1] == '2':
    #                 dp[i] = dp[i-2]
    #                 continue
    #             return 0

    #         if s[i-1] == '1' or (s[i-1] == '2' and '1' <= s[i] <= '6'):
    #             dp[i] = dp[i-1]+dp[i-2]
    #             continue

    #         dp[i] = dp[i-1]

    #     return dp[n-1]

    # def numDecodings(self, s: str) -> int:
    #     # Bottom-up DP : from left to right
    #     # time complexity: O(2^N)
    #     # space complexity: O(N) used for memorization

    #     if s[0] == '0':
    #         return 0

    #     @lru_cache(None)
    #     def dp(i: int) -> int:
    #         if i < 1:
    #             return 1

    #         if s[i] == '0':
    #             if s[i-1] == '1' or s[i-1] == '2':
    #                 return dp(i-2)
    #             return 0

    #         if s[i-1] == '1' or (s[i-1] == '2' and '1' <= s[i] <= '6'):
    #             return dp(i-1)+dp(i-2)

    #         return dp(i-1)

    #     return dp(len(s)-1)

    def numDecodings(self, s: str) -> int:
        # Top-down DP : from left to right
        # time complexity: O(2^N)
        # space complexity: O(N) stack usage

        from functools import lru_cache

        @lru_cache
        def dp(s: str) -> int:
            if not s:
                return 1

            if s[0] == "0":
                return 0

            if len(s) == 1:
                return 1

            if len(s) >= 2:
                if s[0] == "1" or (s[0] == "2" and "0" <= s[1] <= "6"):
                    return dp(s[1:]) + dp(s[2:])

                return dp(s[1:])

        return dp(s)


# @lc code=end
