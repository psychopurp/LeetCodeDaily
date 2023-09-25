#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # add another solution:  i represent the index of zero
        # O(n) time complexity O(1) space complexity
        i = 0
        for k in range(len(nums)):
            if nums[k] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1

# @lc code=end
