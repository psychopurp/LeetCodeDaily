#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time complexity: O(n^2)
        # spcae complexity: O(n)

        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if val == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # 跳过重复的元素
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif val > 0:
                    right -= 1
                else:
                    left += 1

        return result


# @lc code=end
