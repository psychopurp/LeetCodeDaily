#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 时间复杂度O(N)，空间复杂度O(1)
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        pre, prepre = 0, 0
        pre2, prepre2 = 0, 0
        for i in range(len(nums)):
            if i > 0:
                prepre, pre = pre, max(prepre+nums[i], pre)
            if i < len(nums)-1:
                prepre2, pre2 = pre2, max(prepre2+nums[i], pre2)
        return max(pre2, pre)


# @lc code=end
