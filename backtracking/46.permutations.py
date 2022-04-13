#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        # time complexity: O(n*n!)
        # space complexity: O(n)

        def backtrack(step: List[int]):
            if len(step) == len(nums):
                ans.append(step[:])  # used O(n) time complexity
                return

            for i in range(len(nums)):

                if visited[i]:
                    continue

                visited[i] = True
                step.append(nums[i])
                backtrack(step)
                step.pop()
                visited[i] = False

        ans, visited = [], [False for i in nums]
        backtrack([])
        return ans
# @lc code=end
