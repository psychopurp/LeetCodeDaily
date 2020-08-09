#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # 时间复杂度O(numRows**2) 空间复杂度O(numRows**2)
        res = []
        for row in range(numRows):
            tmp = []
            for i in range(row + 1):
                if i == 0 or i == row:
                    tmp.append(1)
                else:
                    tmp.append(res[row - 1][i - 1] + res[row - 1][i])
            res.append(tmp[:])
        return res

        # @lc code=end
