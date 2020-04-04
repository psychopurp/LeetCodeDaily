#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3:
            return []
        result = []
        n = len(nums)
        i, L, R = 0,  1, n - 1

        while i <= n - 3 and nums[i] <= 0:

            if L >= R:
                i_val = nums[i]
                while i <= n-3 and nums[i] == i_val:
                    i += 1
                L = i + 1
                R = n-1
                continue
            val = nums[i] + nums[L] + nums[R]
            if val == 0:
                result.append([nums[i], nums[L], nums[R]])
                low_val, high_val = nums[L], nums[R]
                while L < R and nums[L] == low_val:
                    L += 1
                while L < R and nums[R] == high_val:
                    R -= 1
                continue
            elif val < 0:
                L += 1
                continue
            elif val > 0:
                R -= 1
                continue
        return result

# @lc code=end
