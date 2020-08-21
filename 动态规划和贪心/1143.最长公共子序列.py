#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 时间复杂度O(N*M) 空间复杂度O(N)
        m = len(text1)
        n = len(text2)
        table = [0 for i in range(m+1)]
        for i in range(n):
            pre = 0
            for j in range(1, m+1):
                cur = table[j]
                if text1[j-1] == text2[i]:
                    table[j] = pre+1
                else:
                    table[j] = max(table[j], table[j-1])
                pre = cur
        return table[-1]

    # @lc code=end
