#
# @lc app=leetcode.cn id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#

# @lc code=start
from typing import List


class Solution:
    # def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    #     # 1.Brute force solution, this will exceed the momory limit
    #     # time complexity: (M^2*N^2)
    #     # space complexity: (M^2*N^2)
    #     m, n = len(matrix) + 1, len(matrix[0]) + 1
    #     dp = [
    #         [[[0 for _ in range(n)] for _ in range(m)] for _ in range(n)]
    #         for _ in range(m)
    #     ]

    #     max_val = -float("inf")

    #     for i1 in range(1, m):
    #         for j1 in range(1, n):
    #             dp[i1][j1][i1][j1] = matrix[i1 - 1][j1 - 1]
    #             for i2 in range(i1, m):
    #                 for j2 in range(j1, n):
    #                     dp[i1][j1][i2][j2] = (
    #                         dp[i1][j1][i2][j2 - 1]
    #                         + dp[i1][j1][i2 - 1][j2]
    #                         - dp[i1][j1][i2 - 1][j2 - 1]
    #                         + matrix[i2 - 1][j2 - 1]
    #                     )

    #                     if dp[i1][j1][i2][j2] <= k:
    #                         max_val = max(max_val, dp[i1][j1][i2][j2])
    #     return max_val

    # def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
    #     # 2.Brute force solution with space optimization, this will exceed the time limit
    #     # time complexity: (M^2*N^2)
    #     # space complexity: (M*N)
    #     m, n = len(matrix) + 1, len(matrix[0]) + 1
    #     max_val = -float("inf")

    #     for i1 in range(1, m):
    #         for j1 in range(1, n):
    #             dp = [[0 for _ in range(n)] for _ in range(m)]
    #             dp[i1][j1] = matrix[i1 - 1][j1 - 1]

    #             for i2 in range(i1, m):
    #                 for j2 in range(j1, n):
    #                     dp[i2][j2] = (
    #                         dp[i2 - 1][j2]
    #                         + dp[i2][j2 - 1]
    #                         - dp[i2 - 1][j2 - 1]
    #                         + matrix[i2 - 1][j2 - 1]
    #                     )

    #                     if dp[i2][j2] <= k:
    #                         max_val = max(max_val, dp[i2][j2])
    #     return max_val

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        # 3.Brute force solution with optimization,transforming the problem into an one-dimensional problem
        # time complexity: (M^2*N*N^2)
        # space complexity: (N)

        """
        If we enumerate the upper and lower boundaries of the rectangle and calculate the sum of elements in each column within the boundary, the original problem is transformed into the following one-dimensional problem:
        Given an array of integers and an integer k, calculate the maximum interval sum of the array, requiring that the interval sum does not exceed k.
        """

        def maximum_subarray_below_k(nums: List[int], k: int) -> int:
            # the worst time complexity will be O(N^2)
            n = len(nums) + 1
            # try dp first
            roll_sum = roll_max = nums[0]
            for i in range(1, n - 1):
                if roll_sum > 0:
                    roll_sum += nums[i]
                else:
                    roll_sum = nums[i]

                roll_max = max(roll_max, roll_sum)

            if roll_max <= k:
                return roll_max

            max_val = float("-inf")
            # degenerate to brute-force algorithm
            for i in range(1, n):
                total = 0
                for j in range(i, n):
                    total += nums[j - 1]
                    if total > max_val and total <= k:
                        max_val = total
                    if total == k:
                        return total

            return max_val

        m, n = len(matrix), len(matrix[0])
        max_val = -float("inf")

        # Enumerate the upper boundary
        for i_upper in range(m):
            row_sums = [0 for _ in range(n)]
            # Enumerate the lower boundary
            for i_lower in range(i_upper, m):
                for c in range(n):
                    row_sums[c] += matrix[i_lower][c]
                max_val = max(max_val, maximum_subarray_below_k(row_sums, k))
        return max_val


# @lc code=end
