#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List


class Solution:
    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     # time complexity: O(N*logN)
    #     # spcae complexity: O(1)

    #     nums.sort()

    #     for i in range(len(nums) - 1):
    #         if nums[i] == nums[i+1]:
    #             return True

    #     return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        # time complexity: O(n)
        # space complexity: O(n)

        hash = set()
        for num in nums:
            if num not in hash:
                hash.add(num)
            else:
                return True
        return False
# @lc code=end
