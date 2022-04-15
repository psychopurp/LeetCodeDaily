#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        # space complexity: O(n)
        # time complexity: O(n*2^n)

        def backtrack(way: List[int], index: int):
            ans.append(way[:])

            for i in range(index, len(nums)):
                way.append(nums[i])
                backtrack(way, i+1)
                way.pop()

        ans = []
        backtrack([], 0)
        return ans
# @lc code=end
