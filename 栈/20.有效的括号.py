#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 时间复杂度O(N) 空间复杂度O(N)
        stack = []
        for i in s:
            if i == "(":
                stack.append(")")
            elif i == "[":
                stack.append("]")
            elif i == "{":
                stack.append("}")
            elif stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0
# @lc code=end
