#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List


class Solution:
    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     # backtracking
    #     # space complexity: O(n)
    #     # time complexity: O(n!)

    #     def backtrack(way: List[str], i: int):
    #         if len(way) == n:
    #             ans.append(way[:])
    #             return

    #         for j in range(n):
    #             if column.get(j, False) or pie.get(i-j, False) or na.get(i+j, False):
    #                 continue

    #             column[j] = True
    #             pie[i-j] = True
    #             na[i+j] = True

    #             cur = ["."]*n
    #             cur[j] = "Q"
    #             way.append("".join(cur))

    #             backtrack(way, i+1)
    #             way.pop()

    #             pie[i-j] = False
    #             column[j] = False
    #             na[i+j] = False

    #     column, pie, na = {}, {}, {}

    #     ans = []
    #     backtrack([], 0)
    #     return ans

    # def solveNQueens(self, n: int) -> List[List[str]]:
    #     # backtracking with bit manipulation
    #     # space complexity: O(n) used in call stack
    #     # time complexity: O(n!)

    #     def backtrack(way: List[str], i: int):
    #         nonlocal column, pie, na

    #         if len(way) == n:
    #             ans.append(way[:])
    #             return

    #         for j in range(n):

    #             if 1 << j & column or 1 << i-j+n & pie or 1 << i+j & na:
    #                 continue

    #             column = 1 << j ^ column
    #             pie = 1 << i-j+n ^ pie  # prevent negative result
    #             na = 1 << i+j ^ na

    #             cur = ["."]*n
    #             cur[j] = "Q"
    #             way.append("".join(cur))

    #             backtrack(way, i+1)
    #             way.pop()

    #             column = 1 << j ^ column
    #             pie = 1 << i-j+n ^ pie
    #             na = 1 << i+j ^ na

    #     column, pie, na = 0, 0, 0

    #     ans = []
    #     backtrack([], 0)
    #     return ans

    def solveNQueens(self, n: int) -> List[List[str]]:
        # DFS
        # space complexity: O(n)
        # time complexity: O(n!)

        def dfs(x: int, cols: List[int], xy_diff: List[int], xy_sum: List[int]):
            if x == n:
                ans.append(cols[:])
            for y in range(n):
                if y not in cols and x - y not in xy_diff and x + y not in xy_sum:
                    dfs(x + 1, cols + [y], xy_diff + [x - y], xy_sum + [x + y])

        ans = []
        dfs(0, [], [], [])

        return [["." * i + "Q" + "." * (n - i - 1) for i in col] for col in ans]


# @lc code=end
