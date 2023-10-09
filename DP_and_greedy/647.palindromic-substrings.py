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
    #     for r in range(n):
    #         for l in range(r + 1):
    #             if s[l] == s[r] and (r - l <= 1 or dp[l + 1][r - 1]):
    #                 dp[l][r] = True
    #                 ans += 1

    #     return ans

    def countSubstrings(self, s: str) -> int:
        # expand from middle to two ends
        # time complexity: O(n^2)
        # space complexity: O(1)

        n = len(s)

        def get_count_of_palindrome(l: int, r: int) -> int:
            count = 0
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

            return count

        total = 0
        for i in range(n):
            total = (
                total
                + get_count_of_palindrome(i, i)
                + get_count_of_palindrome(i, i + 1)
            )

        return total


# @lc code=end
