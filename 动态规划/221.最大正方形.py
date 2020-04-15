#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 状态转移：dp(i, j)=min(dp(i−1, j), dp(i−1, j−1), dp(i, j−1))+1
        if not matrix:
            return 0
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = int(matrix[i][j])
                if i == 0 or j == 0:
                    res = max(res, matrix[i][j])
                    continue
                if matrix[i][j] == 0:
                    continue
                matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1]
                                   [j - 1], matrix[i][j - 1]) + 1
                res = max(res, matrix[i][j])
        return res**2


# @lc code=end
