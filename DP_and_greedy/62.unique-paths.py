#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Bottom Up DP
        # time complexity: O(M*N)
        # space complexity: O(M*N)

        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j]+matrix[i][j-1]

        return matrix[m-1][n-1]

    # def uniquePaths(self, m: int, n: int) -> int:
    #     # Top Down DP (correct but TLE)
    #     # time complexity: O(2^(M+N)) each position has two branches.
    #     # space complexity: O(M+N)

    #     def dp(m: int, n: int) -> int:
    #         if m == 1 or n == 1:
    #             return 1

    #         return dp(m, n-1)+dp(m-1, n)

    #     return dp(m, n)

    # def uniquePaths(self, m: int, n: int) -> int:
    #     # Top Down DP : memorization
    #     # time complexity: O(M*N)
    #     # space complexity: O(M*N)

    #     def dp(m: int, n: int) -> int:
    #         if m == 1 or n == 1:
    #             return 1

    #         if (m, n) in memo:
    #             return memo[(m, n)]

    #         memo[(m, n)] = dp(m, n-1)+dp(m-1, n)
    #         return memo[(m, n)]

    #     memo = {}
    #     return dp(m, n)

    # @lc code=end
