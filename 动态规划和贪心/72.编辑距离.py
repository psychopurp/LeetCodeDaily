#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        table = [i for i in range(len(word1)+1)]
        pre = 0
        for i in range(len(word2)):
            pre = i
            for j in range(len(table)):
                if j == 0:
                    table[j] = i+1
                    continue
                if word1[j-1] == word2[i]:
                    tmp = table[j]
                    table[j] = pre
                    pre = tmp
                else:
                    tmp = table[j]
                    table[j] = min(table[j], table[j-1], pre)+1
                    pre = tmp
        return table[-1]

        # @lc code=end
