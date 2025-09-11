#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        # time complexity: O(m*n)
        # space complexity: O(m*n)

        m, n = len(grid), len(grid[0])

        def get_area(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            if grid[i][j] == 1:
                grid[i][j] = 0
                return 1+get_area(i, j+1)+get_area(i, j-1)+get_area(i+1, j)+get_area(i-1, j)

            return 0

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = get_area(i, j)
                    max_area = max(area, max_area)

        return max_area


# @lc code=end
