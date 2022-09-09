#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
from typing import List


class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    #     # 1. Bottom-up DP : pre_min,pre_max represent the minimum and maximum value ending with i
    #     # time complexity: O(N)
    #     # space complexity: O(1)

    #     pre_min = pre_max = max_val = nums[0]
    #     for i in range(1, len(nums)):
    #         max_num = max(nums[i], pre_max*nums[i], pre_min*nums[i])
    #         min_num = min(nums[i], pre_max*nums[i], pre_min*nums[i])
    #         pre_max, pre_min = max_num, min_num
    #         max_val = max(max_val, max_num, min_num)
    #     return max_val

    def maxProduct(self, nums: List[int]) -> int:
        # 2. Bottom-up DP : pre_min,pre_max represent the minimum and maximum value ending with i
        # time complexity: O(N)
        # space complexity: O(1)

        pre_min = pre_max = max_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                pre_max, pre_min = pre_min, pre_max
            max_num = max(nums[i], pre_max*nums[i])
            min_num = min(nums[i], pre_min*nums[i])
            pre_max, pre_min = max_num, min_num
            max_val = max(max_val, max_num, min_num)
        return max_val
# @lc code=end
