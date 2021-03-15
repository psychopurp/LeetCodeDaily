#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     # 方法一：中心扩散法 时间复杂度O(N**2)，空间复杂度O(1)
    #     def expendAroundCenter(s, l, r):
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             l -= 1
    #             r += 1
    #         return s[l+1:r]
    #     res = ""
    #     for i in range(len(s)):
    #         s1 = expendAroundCenter(s, i, i)  # 奇数扩散
    #         s2 = expendAroundCenter(s, i, i + 1)  # 偶数扩散
    #         s3 = s1 if len(s1) > len(s2) else s2
    #         if len(s3) > len(res):
    #             res = s3
    #     return res

    # def longestPalindrome(self, s: str) -> str:
    #     # 方法二：将字符串倒过来，查询公共字串【WARN:这个方法有问题】
    #     n = len(s)
    #     revert = s[::-1]
    #     table = [[0 for _ in range(n+1)] for _ in range(n+1)]
    #     maxIndex = [0, 0]
    #     for i in range(1, n+1):
    #         for j in range(1, n+1):
    #             if s[i-1] == revert[j-1]:
    #                 table[i][j] = table[i-1][j-1]+1
    #                 if table[i][j] > table[maxIndex[0]][maxIndex[1]]:
    #                     maxIndex[0] = i
    #                     maxIndex[1] = j
    #     i, j = maxIndex
    #     res = ""
    #     while table[i][j] != 0:
    #         res += s[i-1]
    #         i -= 1
    #         j -= 1
    #     return res

    # @lc code=end
