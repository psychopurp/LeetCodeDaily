#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start


class Solution:
    def jump(self, nums: List[int]) -> int:
        # end 为选择界限 每次选择能跳最远的
        end = 0
        max_pos = 0
        step = 0

        for i in range(len(nums)-1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                step += 1
                end = max_pos
        return step


# @lc code=end
