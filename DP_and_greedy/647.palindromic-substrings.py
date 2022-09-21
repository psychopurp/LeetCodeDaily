#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start


class Solution:
    # def countSubstrings(self, s: str) -> int:
    #     # brute force : dp[i] represents the amount of palindromic strings of the string ending with i
    #     # time complexity: O(n^3)
    #     # space complexity: O(n)

    #     dp = [1]*(len(s))

    #     def is_valid(l: int, r: int) -> bool:
    #         while l <= r:
    #             if s[l] != s[r]:
    #                 return False

    #             l += 1
    #             r -= 1
    #         return True

    #     for i in range(1, len(s)):
    #         count = 0
    #         for j in range(0, i+1):
    #             if is_valid(j, i):
    #                 count += 1
    #         dp[i] = dp[i-1]+count

    #     return dp[-1]

    # def countSubstrings(self, s: str) -> int:
    #     # dp : dp[i][j] refers to the substring s[i:j+1] whether a palindromic string
    #     # time complexity: O(n^2)
    #     # space complexity: O(n^2)

    #     n = len(s)
    #     dp = [[False for _ in range(n)] for _ in range(n)]
    #     ans = 0

    #     for j in range(n):
    #         for i in range(j+1):
    #             if s[i] == s[j] and (j-i <= 1 or dp[i+1][j-1]):
    #                 dp[i][j] = True
    #                 ans += 1

    #     return ans

    def countSubstrings(self, s: str) -> int:
        # dp : dp[i][j] refers to the substring s[i:j+1] whether a palindromic string
        # time complexity: O(n^2)
        # space complexity: O(1)

        def valid_len(l: int, r: int) -> int:
            cnt = 0

            while r < n and l >= 0 and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        n = len(s)
        ans = 0

        for i in range(n):
            ans += valid_len(i, i)
            if i < n-1:
                ans += valid_len(i, i+1)
        return ans
        # dp(len)


# @lc code=end
