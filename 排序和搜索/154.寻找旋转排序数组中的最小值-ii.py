#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start


class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] < nums[right] or left == right:
                return nums[left]
            mid = (left + right) // 2
            if nums[left] == nums[mid]:
                left += 1
                continue
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid


# @lc code=end
