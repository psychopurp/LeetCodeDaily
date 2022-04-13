#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        # time complexity: O(n*n!)
        # space complexity: O(n) used in recursive stack depth

        def backtrack(step: List[int]):
            if len(step) == len(nums):
                ans.append(step[:])
                return

            for i in range(len(nums)):
                if not visited[i]:

                    if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                        continue

                    visited[i] = True
                    step.append(nums[i])
                    backtrack(step)
                    step.pop()
                    visited[i] = False

        ans, visited = [], [False for _ in nums]
        nums.sort()
        backtrack([])
        return ans
# @lc code=end
