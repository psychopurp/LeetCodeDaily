#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # backtracking
        # time complexity: O(c(n^k)*k)
        # space complexity: O(n)

        def backtrack(start: int, step: List[int]):
            # pruning
            if (n+1-start)+len(step) < k:
                return

            if len(step) == k:
                ans.append(step[:])  # time complexity O(k)
                return

            for i in range(start, n+1):
                step.append(i)
                backtrack(i+1, step)
                step.pop()

        ans = []
        backtrack(1, [])
        return ans
# @lc code=end
