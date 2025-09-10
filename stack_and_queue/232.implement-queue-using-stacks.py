#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from collections import deque


class MyQueue:

    def __init__(self):
        self.in_stack=deque()
        self.out_stack=deque()
        

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        

    def pop(self) -> int:
        peek=self.peek()
        self.out_stack.pop()
        return peek

    def peek(self) -> int:
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]


    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack
    
    # in: [1,2,3,4] out:[]
    # in:[] out:[4,3,2] pop:1
    # in:[5] out:[4,3,2]

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

