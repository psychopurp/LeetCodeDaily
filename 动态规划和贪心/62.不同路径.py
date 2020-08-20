#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 空间复杂度O(N)，时间复杂度O(M*N)
        table = [1 for i in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                table[j] = table[j]+table[j-1]
        return table[-1]

# @lc code=end
