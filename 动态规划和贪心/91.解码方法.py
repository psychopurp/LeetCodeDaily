#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # 时间复杂度O(N) 空间复杂度O(1)
        if s[0] == "0":
            return 0
        pre, pre_pre = 1, 1
        for i in range(1, len(s)):
            tmp = pre
            if s[i] == "0":
                if s[i-1] == "1" or s[i-1] == "2":
                    pre = pre_pre
                else:
                    return 0
            elif s[i-1] == "1" or s[i-1] == "2" and "1" <= s[i] <= "6":
                pre = pre+pre_pre
            pre_pre = tmp
        return pre
        # @lc code=end
