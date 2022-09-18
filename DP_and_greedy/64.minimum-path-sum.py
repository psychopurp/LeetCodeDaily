#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from functools import lru_cache
from typing import List


class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     # 1. Top-down DP : memorization
    #     # time complexity: O(M*N)
    #     # space complexity: O(M*N)

    #     m = len(grid)
    #     n = len(grid[0])

    #     @lru_cache(None)
    #     def dp(i: int, j: int) -> int:
    #         if i == m-1 and j == n-1:
    #             return grid[i][j]

    #         if i >= m or j >= n:
    #             return float("inf")

    #         val = min(dp(i+1, j), dp(i, j+1))+grid[i][j]
    #         return val

    #     return dp(0, 0)

    def minPathSum(self, grid: List[List[int]]) -> int:
        # 2. Bottom-up DP
        # time complexity: O(M*N)
        # space complexity: O(M*N)

        m = len(grid)
        n = len(grid[0])

        def get_val(i: int, j: int) -> int:
            if i >= m or j >= n:
                return float('inf')
            return grid[i][j]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                grid[i][j] = min(get_val(i, j+1), get_val(i+1, j))+grid[i][j]

        return grid[0][0]


# @lc code=end
