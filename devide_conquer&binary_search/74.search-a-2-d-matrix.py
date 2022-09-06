#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        # time complexity: O(log (m+n))
        # space complexity: O(1)

        m, n = len(matrix), len(matrix[0])
        l, r = 0, m*n-1

        while l <= r:
            mid = (l+r)//2
            val = matrix[mid//n][mid % n]
            if val == target:
                return True

            if val > target:
                r = mid-1
            else:
                l = mid+1
        return False


# @lc code=end
