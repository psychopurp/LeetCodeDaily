#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 空间复杂度O(N)，时间复杂度O(M*N)
        m = len(obstacleGrid[0])
        n = len(obstacleGrid)
        table = [1 for i in range(m)]

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    table[j] = 0
                    continue
                if j == m-1:
                    continue
                if i == n-1:
                    table[j] = table[j+1]
                    continue
                table[j] += table[j+1]
        return table[0]
        # @lc code=end
