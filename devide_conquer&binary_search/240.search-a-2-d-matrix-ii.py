#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] Search a 2D Matrix II
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # time complexity: O(m+n)
        # space complexity: O(1)
        
        m, n = len(matrix), len(matrix[0])
        x, y = 0, n-1

        while x < m and y >= 0:
            val = matrix[x][y]
            if val == target:
                return True

            if val > target:
                y -= 1
            else:
                x += 1

        return False

# @lc code=end
