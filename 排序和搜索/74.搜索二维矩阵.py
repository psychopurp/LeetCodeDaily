#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:

            mid = (left + right) // 2
            x, y = mid // n, mid % n
            if matrix[x][y] == target:
                return True
            if target < matrix[x][y]:
                right = mid - 1
            else:
                left = mid + 1
        return False

# @lc code=end
