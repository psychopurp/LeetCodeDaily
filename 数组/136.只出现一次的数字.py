#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
# 通过异或运算
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            result ^=i
        return result
# @lc code=end

