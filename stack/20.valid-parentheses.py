#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # stack
        # time complexity: O(n)
        # space complexity: O(n)

        stack = []

        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif stack and stack[-1] == c:
                stack.pop()
            else:
                return False

        return len(stack) == 0


# @lc code=end
