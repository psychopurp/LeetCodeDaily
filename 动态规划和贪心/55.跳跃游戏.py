#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start


class Solution:
    # def canJump(self, nums: List[int]) -> bool:

    #     right = 0
    #     for i in range(len(nums)):
    #         if i <= right:
    #             right = max(right, i + nums[i])
    #             if right >= len(nums) - 1:
    #                 return True
    #     return False

    def canJump(self, nums: List[int]) -> bool:
        # 从后开始遍历
        last = len(nums) - 1
        i = last - 1
        while i >= 0:
            if i + nums[i] >= last:
                last = i
            i -= 1
        return last == 0

        # @lc code=end
