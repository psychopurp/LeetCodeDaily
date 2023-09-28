#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N-Queens II
#


# @lc code=start
from typing import List


class Solution:
    # def totalNQueens(self, n: int) -> int:
    #     # DFS
    #     # space complexity: O(n)
    #     # time complexity: O(n!)

    #     def dfs(row: int, cols: List[int], xy_diff: List[int], xy_sum: List[int]):
    #         if row == n:
    #             nonlocal total
    #             total += 1
    #             return

    #         for col in range(n):
    #             if (
    #                 col not in cols
    #                 and (row - col) not in xy_diff
    #                 and (row + col) not in xy_sum
    #             ):
    #                 dfs(
    #                     row + 1,
    #                     cols + [col],
    #                     xy_diff + [row - col],
    #                     xy_sum + [row + col],
    #                 )

    #     total = 0
    #     dfs(0, [], [], [])
    #     return total

    # def totalNQueens(self, n: int) -> int:
    #     # DFS with space optimization by using bit to store set
    #     # space complexity: O(1)
    #     # time complexity: O(n!)

    #     def dfs(row: int, cols: int, xy_diff: int, xy_sum: int):
    #         if row == n:
    #             nonlocal total
    #             total += 1
    #             return

    #         for col in range(n):
    #             # row-col+n : +n used to prevent negative result
    #             if (
    #                 not (1 << col) & cols
    #                 and not (1 << (row - col + n)) & xy_diff
    #                 and not (1 << (row + col)) & xy_sum
    #             ):
    #                 dfs(
    #                     row + 1,
    #                     cols | (1 << col),
    #                     xy_diff | (1 << (row - col + n)),
    #                     xy_sum | (1 << (row + col)),
    #                 )

    #     total = 0
    #     dfs(0, 0, 0, 0)
    #     return total

    def totalNQueens(self, n: int) -> int:
        # Final optimization
        # DFS with space optimization by using bit to store set
        # space complexity: O(1)
        # time complexity: O(n!)

        def dfs(row: int, cols: int, xy_diff: int, xy_sum: int):
            if row == n:
                nonlocal total
                total += 1
                return

            # find available spaces
            bits = (~(cols | xy_diff | xy_sum)) & ((1 << n) - 1)

            while bits:
                p = bits & -bits  # get the lowest one
                bits = bits & (bits - 1)  # clear the lowest one
                dfs(row + 1, cols | p, (xy_diff | p) << 1, (xy_sum | p) >> 1)

        total = 0
        dfs(0, 0, 0, 0)
        return total


# @lc code=end
