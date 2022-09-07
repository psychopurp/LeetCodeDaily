#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     # Bottom-up DP
    #     # time complexity: O(M*N)
    #     # space complexity: O(M*N)

    #     m, n = len(text1), len(text2)
    #     matrix = [[0 for _ in range(n+1)] for _ in range(m+1)]

    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if text1[i-1] == text2[j-1]:
    #                 matrix[i][j] = matrix[i-1][j-1]+1
    #             else:
    #                 matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    #     return matrix[-1][-1]

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     # Top-down DP (connrect but TLE)
    #     # time complexity: O(2^(M+N))
    #     # space complexity: O(M+N)

    #     if not text1 or not text2:
    #         return 0

    #     if text1[-1] == text2[-1]:
    #         return self.longestCommonSubsequence(text1[:-1], text2[:-1])+1

    #     return max(self.longestCommonSubsequence(
    #         text1[:-1], text2), self.longestCommonSubsequence(text1, text2[:-1]))

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top-down DP with memorization
        # time complexity: O(M*N)
        # space complexity: O(M*N)

        def dp(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = dp(i-1, j-1)+1
            else:
                memo[(i, j)] = max(dp(i-1, j), dp(i, j-1))

            return memo[(i, j)]
        memo = {}
        return dp(len(text1)-1, len(text2)-1)


# @lc code=end
