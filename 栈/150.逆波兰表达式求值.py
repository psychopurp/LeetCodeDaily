#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operations = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: x-y,
            '*': lambda x, y: x*y,
            '/': lambda x, y: int(x/y)
        }

        for i in tokens:
            if i not in operations.keys():
                stack.append(int(i))
            else:
                second = stack.pop()
                first = stack.pop()
                stack.append(operations[i](first, second))
        return stack[-1]


# @lc code=end
