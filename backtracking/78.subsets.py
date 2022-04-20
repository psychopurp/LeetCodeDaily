#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     # backtracking
    #     # space complexity: O(n)
    #     # time complexity: O(n*2^n)

    #     def backtrack(way: List[int], index: int):
    #         ans.append(way[:])

    #         for i in range(index, len(nums)):
    #             way.append(nums[i])
    #             backtrack(way, i+1)
    #             way.pop()

    #     ans = []
    #     backtrack([], 0)
    #     return ans

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     # Iterative
    #     # space complexity: O(n)
    #     # time complexity: O(n*2^n)

    #     ans = [[]]

    #     for num in nums:

    #         newSubset = []
    #         for subset in ans:
    #             newSubset.append(subset+[num])

    #         ans.extend(newSubset)

    #     return ans

    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     # bit manipulation
    #     # space complexity: O(n)
    #     # time complexity: O(n*2^n)

    #     ans = []

    #     i = 0
    #     while i < (1 << len(nums)):
    #         subset = []
    #         for j in range(len(nums)):
    #             if i >> j & 1:
    #                 subset.append(nums[j])
    #         ans.append(subset[:])
    #         i += 1
    #     return ans

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking
        # space complexity: O(n)
        # time complexity: O(n*2^n)

        def backtrack(way: List[int], index: int):
            if index == len(nums):
                ans.append(way[:])
                return

            backtrack(way, index+1)
            way.append(nums[index])
            backtrack(way, index+1)
            way.pop()

        ans = []
        backtrack([], 0)
        return ans

# @lc code=end
