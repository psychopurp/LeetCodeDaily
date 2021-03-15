#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 时间复杂度O(N)
        start, end = 0, len(numbers)-1
        while start <= end:
            if numbers[start]+numbers[end] > target:
                end -= 1
            elif numbers[start]+numbers[end] < target:
                start += 1
            elif numbers[start]+numbers[end] == target:
                return [start+1, end+1]
# @lc code=end
