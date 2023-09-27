#
# @lc app=leetcode.cn id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#

# @lc code=start
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # basic BFS solution
        # time complexity: O(N^2)
        # space complexity: O(N^2)

        from collections import deque

        if grid[0][0] == 1:
            return -1

        n = len(grid)
        visited = set([(0, 0)])
        q = deque([(0, 0)])
        level = 0

        while q:
            level += 1
            for _ in range(len(q)):
                pos = q.popleft()
                if pos == (n - 1, n - 1):
                    return level

                for direction in [
                    (0, 1),
                    (0, -1),
                    (-1, 0),
                    (1, 0),
                    (-1, 1),
                    (-1, -1),
                    (1, -1),
                    (1, 1),
                ]:
                    x, y = pos[0] + direction[0], pos[1] + direction[1]
                    if (
                        0 <= x < n
                        and 0 <= y < n
                        and grid[x][y] == 0
                        and (x, y) not in visited
                    ):
                        if (x, y) == (n - 1, n - 1):
                            return level + 1

                        visited.add((x, y))
                        q.append((x, y))
        return -1


# @lc code=end
