#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_val = 0

        for i in range(len(grid)):

            for j in range(len(grid[0])):
                tmp_max = 0
                if grid[i][j] == -1:
                    continue
                stack = []
                if grid[i][j] == 1:
                    grid[i][j] = -1
                    stack.append((i, j))
                while stack:
                    row, col = stack.pop()
                    tmp_max += 1
                    if 0 <= row - 1 < len(grid) and grid[row - 1][col] == 1:
                        grid[row - 1][col] = -1
                        stack.append((row - 1, col))
                    if 0 <= row + 1 < len(grid) and grid[row + 1][col] == 1:
                        grid[row+1][col] = -1
                        stack.append((row + 1, col))
                    if 0 <= col - 1 < len(grid[0]) and grid[row][col - 1] == 1:
                        grid[row][col-1] = -1
                        stack.append((row, col-1))
                    if 0 <= col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                        grid[row][col+1] = -1
                        stack.append((row, col + 1))
                if tmp_max > max_val:
                    max_val = tmp_max
                grid[i][j] = -1
        return max_val
        # @lc code=end
