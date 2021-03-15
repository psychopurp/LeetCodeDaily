#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    # def missingNumber(self, nums: List[int]) -> int:
    #     # 数学方法 时间复杂度O(N) 空间复杂度O(1)
    #     total = 0
    #     for i in range(len(nums)):
    #         total += i
    #         total -= nums[i]
    #     total += len(nums)
    #     return total

    def missingNumber(self, nums: List[int]) -> int:
        # 位方法 时间复杂度O(N) 空间复杂度O(1)
        miss = len(nums)
        for i in range(miss):
            miss ^= i ^ nums[i]
        return miss


# @lc code=end
