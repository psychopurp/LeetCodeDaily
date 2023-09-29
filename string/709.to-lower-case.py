#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] To Lower Case
#


# @lc code=start
class Solution:
    # def toLowerCase(self, s: str) -> str:
    #     # 1. Use the language api
    #     # time complexity: O(N)
    #     # space complexity: O(1)
    #     return s.lower()

    def toLowerCase(self, s: str) -> str:
        # 2. Use bit operation
        # time complexity: O(N)
        # space complexity: O(1)

        ret = []
        for i in range(len(s)):
            if "A" <= s[i] <= "Z":
                ret.append(chr(ord(s[i]) | 32))
            else:
                ret.append(s[i])
        return "".join(ret)


# @lc code=end
