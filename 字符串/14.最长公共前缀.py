#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        pattern = strs[0]
        index = len(pattern)
        for i in strs[1:]:
            j = 0
            tmp_len = 0
            while j < min(len(pattern), len(i)) and pattern[j] == i[j]:
                tmp_len += 1
                j += 1
            index = tmp_len
            pattern = pattern[:index]
        return pattern[:index]
        # @lc code=end
