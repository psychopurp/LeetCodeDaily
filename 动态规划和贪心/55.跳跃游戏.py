#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        right = 0
        for i in range(len(nums)):
            if i <= right:
                right = max(right, i + nums[i])
                if right >= len(nums) - 1:
                    return True
        return False
        # @lc code=end
