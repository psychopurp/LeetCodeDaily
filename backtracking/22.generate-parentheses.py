# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     # backtracking
    #     # time complexity: O(2^n)
    #     # space complexity: O(n)

    #     def backtrack(left: int, right: int, step: List[str]):

    #         if left == 0 and right == 0:
    #             ans.append("".join(step))
    #             return

    #         if left > 0:
    #             step.append("(")
    #             backtrack(left-1, right, step)
    #             step.pop()

    #         if right > left:
    #             step.append(")")
    #             backtrack(left, right-1, step)
    #             step.pop()

    #     ans = []
    #     backtrack(n, n, [])
    #     return ans

    def generateParenthesis(self, n: int) -> List[str]:
        # backtracking : BFS with queue
        # time complexity: O(2^n)
        # space complexity: O(n)

        from collections import deque

        q = deque()
        ans = []

        q.append((0, 0, ''))

        while q:
            left, right, step = q.popleft()
            if left == n and right == n:
                ans.append(step)
                continue

            if left < n:
                q.append((left+1, right, step+"("))
            if right < left:
                q.append((left, right+1, step+")"))

        return ans

# @lc code=end
