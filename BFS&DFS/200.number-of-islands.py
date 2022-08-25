#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List, Tuple


class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     # DFS : first solution of mine
    #     # time complexity: O(M*N)
    #     # space complexity: O(M*N)

    #     visited = set()
    #     directions: List[Tuple[int, int]] = [
    #         (0, -1), (0, 1), (1, 0), (-1, 0)]

    #     def dfs(pos: Tuple[int, int]):
    #         visited.add(pos)
    #         for d in directions:
    #             np = (x, y) = (pos[0]+d[0], pos[1]+d[1])
    #             if x < 0 or x >= m or y < 0 or y >= n:
    #                 continue

    #             if np not in visited and grid[x][y] == "1":
    #                 dfs(np)

    #     m, n = len(grid), len(grid[0])
    #     island = 0

    #     for i in range(m):
    #         for j in range(n):
    #             if (i, j) not in visited:
    #                 if grid[i][j] == "1":
    #                     dfs((i, j))
    #                     island += 1

    #     return island

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     # DFS
    #     # time complexity: O(M*N)
    #     # space complexity: O(M*N)

    #     m, n = len(grid), len(grid[0])

    #     def dfs(x: int, y: int):
    #         if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
    #             return
    #         grid[x][y] = "0"
    #         dfs(x-1, y)
    #         dfs(x+1, y)
    #         dfs(x, y-1)
    #         dfs(x, y+1)
    #     num = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == "1":
    #                 dfs(i, j)
    #                 num += 1

    #     return num

    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS version of solution 2
        # time complexity: O(M*N)
        # space complexity: O(M*N)

        m, n = len(grid), len(grid[0])
        from collections import deque

        def bfs(x: int, y: int):
            q = deque([(x, y)])

            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == "0":
                        continue

                    grid[x][y] = "0"
                    q.append((x-1, y))
                    q.append((x+1, y))
                    q.append((x, y-1))
                    q.append((x, y+1))

        num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    bfs(i, j)
                    num += 1

        return num
# @lc code=end
