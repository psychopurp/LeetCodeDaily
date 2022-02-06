#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    # def __init__(self):
    #     self._stack = []
    #     self._minStack = []

    # def push(self, val: int) -> None:
    #     self._stack.append(val)
    #     if not self._minStack or val <= self._minStack[-1]:
    #         self._minStack.append(val)

    # def pop(self) -> None:
    #     val = self._stack.pop()
    #     if self._minStack and val == self._minStack[-1]:
    #         self._minStack.pop()

    # def top(self) -> int:
    #     return self._stack[-1]

    # def getMin(self) -> int:
    #     return self._minStack[-1]

    def __init__(self):
        self._stack = []

    def push(self, val: int) -> None:
        minVal = val
        if self._stack and val > self._stack[-1][1]:
            minVal = self._stack[-1][1]
        self._stack.append((val, minVal))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def getMin(self) -> int:
        return self._stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
