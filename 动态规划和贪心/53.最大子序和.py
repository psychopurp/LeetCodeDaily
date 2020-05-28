#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#

# @lc code=start


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     # 使用dp[i]表示以索引i为结尾的连续子数组的最大和
    #     dp = []
    #     for i in range(len(nums)):
    #         if not dp:
    #             dp.append(nums[i])
    #         else:
    #             val = max(nums[i], dp[i-1]+nums[i])
    #             dp.append(val)
    #     return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        # 贪心算法
        ans = float('-inf')
        summ = 0

        for i in range(len(nums)):
            summ += nums[i]
            ans = max(ans, summ)
            if summ < 0:
                summ = 0

        return ans


# @lc code=end
