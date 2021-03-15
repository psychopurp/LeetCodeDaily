#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 时间复杂度O(MN) 空间复杂度O(N)
        table = grid[0][:]
        for i in range(1, len(table)):
            table[i] = table[i-1]+table[i]
        for i in range(1, len(grid)):
            for j in range(len(grid[i])):
                if j > 0:
                    table[j] = min(table[j], table[j-1])+grid[i][j]
                else:
                    table[j] = table[j]+grid[i][j]
        return table[-1]

# @lc code=end
