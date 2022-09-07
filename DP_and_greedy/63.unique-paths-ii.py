#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List


class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     # Bottom Up DP
    #     # time complexity: O(M*N)
    #     # space complexity: O(M*N)

    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     matrix = [[0 for _ in range(n)] for _ in range(m)]

    #     matrix[0][0] = 0 if obstacleGrid[0][0] == 1 else 1

    #     for i in range(m):
    #         for j in range(n):
    #             if obstacleGrid[i][j] == 0:
    #                 if i > 0 and j > 0:
    #                     matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]
    #                 elif i > 0:
    #                     matrix[i][j] = matrix[i-1][j]
    #                 elif j > 0:
    #                     matrix[i][j] = matrix[i][j-1]

    #     return matrix[m-1][n-1]

    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     # 1. Top Down DP : memorization
    #     # time complexity: O(M*N)
    #     # space complexity: O(M*N)

    #     def dp(i: int, j: int) -> int:
    #         if obstacleGrid[i][j] == 1:
    #             return 0

    #         if i == 0 and j == 0:
    #             return 1

    #         if (i, j) in memo:
    #             return memo[(i, j)]

    #         val = 0

    #         if i > 0 and j > 0:
    #             val = dp(i-1, j)+dp(i, j-1)
    #         elif i > 0:
    #             val = dp(i-1, j)
    #         elif j > 0:
    #             val = dp(i, j-1)

    #         memo[(i, j)] = val
    #         return val

    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     memo = {}
    #     return dp(m-1, n-1)

    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    #     # Bottom Up DP : space optimized
    #     # time complexity: O(M*N)
    #     # space complexity: O(N)

    #     m, n = len(obstacleGrid), len(obstacleGrid[0])
    #     matrix = [0 for _ in range(n)]

    #     pre = 0 if obstacleGrid[0][0] == 1 else 1

    #     for i in range(m):
    #         for j in range(n):
    #             if obstacleGrid[i][j] == 0:
    #                 if i > 0 and j > 0:
    #                     matrix[j] = pre+matrix[j]
    #                 else:
    #                     matrix[j] = pre
    #                 pre = matrix[j]
    #             else:
    #                 matrix[j] = 0
    #                 pre = 0
    #         pre = matrix[0]

    #     return matrix[-1]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 2. Top Down DP : memorization
        # time complexity: O(M*N)
        # space complexity: O(M*N)

        def dp(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0

            # reach the end
            if i == m-1 and j == n-1:
                return 1

            memo[(i, j)] = dp(i+1, j)+dp(i, j+1)
            return memo[(i, j)]
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        return dp(0, 0)

# @lc code=end
