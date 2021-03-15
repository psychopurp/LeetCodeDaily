#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, cur, p2 = 0, 0, len(nums)-1
        while cur <= p2:
            if nums[cur] == 2:
                nums[p2], nums[cur] = nums[cur], nums[p2]
                p2 -= 1
            elif nums[cur] == 0:
                nums[p0], nums[cur] = nums[cur], nums[p0]
                cur += 1
                p0 += 1
            else:
                cur += 1

                # @lc code=end
