#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     # Bottom-up DP : dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    #     # time complexity: O(m*n)
    #     # space complexity: O(1)

    #     max_val = 0

    #     def get_val(i: int, j: int) -> int:
    #         if i < 0 or j < 0:
    #             return 0

    #         return int(matrix[i][j])

    #     for i in range(len(matrix)):
    #         for j in range(len(matrix[0])):
    #             if matrix[i][j] == "0":
    #                 continue

    #             matrix[i][j] = str(
    #                 min(get_val(i-1, j), get_val(i, j-1), get_val(i-1, j-1))+1)
    #             max_val = max(max_val, int(matrix[i][j]))
    #     return max_val*max_val

    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    #     # Top-down DP : dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
    #     # time complexity: O(m*n)
    #     # space complexity: O(m+n)

    #     @lru_cache(None)
    #     def dp(i: int, j: int) -> int:
    #         nonlocal max_val

    #         if i < 0 or j < 0:
    #             return 0

    #         val = min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1))+1

    #         if matrix[i][j] == "0":
    #             return 0

    #         max_val = max(max_val, val)
    #         return val

    #     max_val = 0
    #     dp(len(matrix)-1, len(matrix[0])-1)
    #     return max_val*max_val

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Bottom-up DP
        # time complexity: O(m*n)
        # space complexity: O(m+n)
        """
        dp[i][j]: maximum square length of (i,j)
        dp[i][j] = min(dp[i-l][j],dp[i][j-l],dp[i-l][j-l]) + dp[i][j]

        l=dp[i][j] l=length of the square
        """

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        max_val = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    max_val = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    l = dp[i][j]

                    if dp[i - l][j] and dp[i][j - l] and dp[i - l][j - l]:
                        dp[i][j] += min(dp[i - l][j], dp[i][j - l], dp[i - l][j - l])
                        max_val = max(max_val, dp[i][j] ** 2)

        return max_val


# @lc code=end
