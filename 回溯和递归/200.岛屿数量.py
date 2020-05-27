#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start


class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
    #     # DFS解法 时间复杂度O(MN) 空间复杂度O(MN)
    #     if not grid:
    #         return 0
    #     row = len(grid)
    #     col = len(grid[0])
    #     count = 0

    #     def dfs(i, j):
    #         if grid[i][j] == '0':
    #             return

    #         grid[i][j] = '0'
    #         # 遍历上下左右四个节点
    #         if i > 0:
    #             dfs(i-1, j)
    #         if i < row - 1:
    #             dfs(i + 1, j)
    #         if j > 0:
    #             dfs(i, j - 1)
    #         if j < col - 1:
    #             dfs(i, j + 1)

    #     for i in range(row):
    #         for j in range(col):
    #             if grid[i][j] == '0':
    #                 continue
    #             else:
    #                 dfs(i, j)
    #                 count += 1
    #     return count

    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS解法 时间复杂度O(MN) 空间复杂度O(MN)
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        count = 0
        from collections import deque
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    while queue:
                        r, c = queue.popleft()
                        grid[r][c] = '0'
                        for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                            if 0 <= x < row and 0 <= y < col and grid[x][y] == '1':
                                queue.append((x, y))
                                grid[x][y] = "0"

        return count

# @lc code=end
