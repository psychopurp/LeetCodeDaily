#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 时间复杂度O(n*2) 空间复杂度O(n)
        table = [triangle[0][0]]
        for i in range(1, len(triangle)):
            m = len(triangle[i])
            new_table = []
            for j in range(m):
                cur = triangle[i][j]
                if j == 0:
                    new_table.append(cur+table[j])
                elif j == m-1:
                    new_table.append(cur+table[j-1])
                else:
                    new_table.append(cur+min(table[j], table[j-1]))
            table = new_table
        return min(table)

        # @lc code=end
