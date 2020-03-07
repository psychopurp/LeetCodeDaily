#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %=len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)


    def reverse(self,nums,start,end):
        while end>start:
            tmp=nums[end]
            nums[end]=nums[start]
            nums[start]=tmp
            start+=1
            end-=1
# @lc code=end
