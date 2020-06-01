#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []

        for x in S:
            if not stack:
                stack.append(x)
            elif x == stack[-1]:
                while stack and stack[-1] == x:
                    stack.pop()
            else:
                stack.append(x)
        return ''.join(stack)

# @lc code=end
