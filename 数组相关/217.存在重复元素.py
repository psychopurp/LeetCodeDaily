#
# @lc app=leetcode.cn id=217 lang=python3
#
# [217] 存在重复元素
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
# # @lc code=end