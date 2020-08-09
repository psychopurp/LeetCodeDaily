#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     amount = []
    #     def backtrack(room, cur):
    #         if room >= len(nums):
    #             amount.append(sum(cur))

    #         for id in range(room, len(nums)):
    #             cur.append(nums[id])
    #             backtrack(id + 2, cur)
    #             cur.pop()
    #     backtrack(0, [])
    #     return max(amount)

    def rob(self, nums: List[int]) -> int:
        pre = 0
        prepre = 0
        amount = 0
        for i in range(len(nums)):
            cur = nums[i]
            amount = max(prepre + cur, pre, amount)
            prepre = pre
            pre = amount
        return amount

        # @lc code=end
