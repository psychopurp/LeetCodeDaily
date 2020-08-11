#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 滑动窗口
        index = 0
        maxLen = 0
        if len(s) <= 1:
            return len(s)
        for i in range(len(s)):
            if s[i] in s[index:i]:
                maxLen = max(maxLen, i-index)
                while s[i] in s[index:i]:
                    index += 1
            else:
                maxLen = max(maxLen, i-index+1)
        return maxLen
# @lc code=end
