#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        start, end = 0, 0
        total = 0
        l = len(nums)+1

        while end < len(nums):
            total += nums[end]

            while total >= s:
                l = min(l, (end - start)+1)
                total -= nums[start]
                start += 1
                continue

            end += 1
        return 0 if l == len(nums)+1 else l


# @lc code=end
