#
# @lc app=leetcode.cn id=980 lang=python3
#
# [980] Unique Paths III
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # DFS solution
        # time complexity: (3^(M*N)) : each node has at most 3 leaf nodes
        # space complexity: (M*N) stack usage
        m, n = len(grid), len(grid[0])
        should_visit = 0
        start = (0, 0)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    start = (i, j)

                if grid[i][j] != -1:
                    should_visit += 1

        def dfs(i: int, j: int, left_visit: int):
            if grid[i][j] == 1:
                if left_visit == 0:
                    nonlocal ans
                    ans += 1
                return

            # set visited
            grid[i][j] = -1
            for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                x, y = i + direction[0], j + direction[1]
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                    dfs(x, y, left_visit - 1)

            # reset visited
            grid[i][j] = 0

        ans = 0
        dfs(start[0], start[1], should_visit - 1)
        return ans


# @lc code=end
