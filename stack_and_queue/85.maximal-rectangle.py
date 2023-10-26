#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # 1.Monotonic stack
        # time complexity: O(N^2)
        # space complexity: O(N)

        """
        Change 2D array to 1D so that can convert this problem to problem.84

        Explanation: https://leetcode.cn/problems/maximal-rectangle/solutions/1/by-ac_oier-k02i/
        """

        m, n = len(matrix), len(matrix[0])
        max_val = 0

        row = [0 for _ in range(n + 1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    row[j] = row[j] + 1
                else:
                    row[j] = 0

            # Monotonic stack to find the maximum rectangle of an 1D array.
            # Each item in the row represents the height
            stack = []
            for k in range(len(row)):
                while stack and row[stack[-1]] > row[k]:
                    h = row[stack.pop()]
                    l = stack[-1] if stack else -1
                    max_val = max(max_val, (k - l - 1) * h)
                stack.append(k)
        return max_val


# @lc code=end
