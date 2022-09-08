#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Bottom-up DP: in-place
        # time complexity: O(N*N)
        # space complexity: O(1)
        m = len(triangle)
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])

        return triangle[0][0]

    # def minimumTotal(self, triangle: List[List[int]]) -> int:
    #     # Top-down DP
    #     # time complexity: O(N*N)
    #     # space complexity: O(N!)

    #     def dp(i: int, j: int) -> int:
    #         if i == len(triangle)-1:
    #             return triangle[i][j]

    #         if (i, j) in memo:
    #             return memo[(i, j)]

    #         memo[(i, j)] = min(dp(i+1, j), dp(i+1, j+1))+triangle[i][j]
    #         return memo[(i, j)]
    #     memo = {}
    #     return dp(0, 0)
# @lc code=end
