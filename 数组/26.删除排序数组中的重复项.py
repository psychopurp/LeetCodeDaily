#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        for fast, k in enumerate(nums):
            if nums[slow] == nums[fast]:
                continue
            else:
                slow+=1
                nums[slow]=nums[fast]
        return slow+1

                
            
# @lc code=end
