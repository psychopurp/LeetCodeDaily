#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
from typing import List


class Solution:
    # def splitArray(self, nums: List[int], k: int) -> int:
    #     # 1.Top-down DP: this will TLE!
    #     # time complexity: O(K*N^2) N=len(nums) K=k
    #     # space complexity: O(N*K)

    #     """
    #     dp(i,k) represents the The minimum value of the sum of the largest continuous subarray obtained by dividing the number of i before the array into k segments
    #     """

    #     from functools import lru_cache

    #     n = len(nums)
    #     pre_sum = [nums[i] for i in range(n)]
    #     for i in range(1, n):
    #         pre_sum[i] = pre_sum[i - 1] + nums[i]

    #     @lru_cache(None)
    #     def dp(r: int, k: int) -> int:
    #         if k == 1:
    #             return pre_sum[r]

    #         val = float("inf")
    #         for i in range(0, r + 1):
    #             left = pre_sum[r] - pre_sum[i]
    #             right = dp(i, k - 1)
    #             val = min(val, max(left, right))
    #         return val

    #     return dp(n - 1, k)

    # def splitArray(self, nums: List[int], k: int) -> int:
    #     # 2.Bottom-up DP: this will TLE!
    #     # time complexity: O(K*N^2) N=len(nums) K=k
    #     # space complexity: O(N*K)

    #     """
    #     dp(i,k) represents the The minimum value of the sum of the largest continuous subarray obtained by dividing the number of i before the array into k segments
    #     """

    #     n = len(nums)
    #     pre_sum = [nums[i] for i in range(n)]
    #     for i in range(1, n):
    #         pre_sum[i] = pre_sum[i - 1] + nums[i]

    #     dp = [[float("inf") for _ in range(k + 1)] for _ in range(n)]

    #     for i in range(n):
    #         dp[i][1] = pre_sum[i]

    #     for k in range(2, k + 1):
    #         for r in range(n):
    #             for l in range(r):
    #                 left = dp[l][k - 1]
    #                 right = pre_sum[r] - pre_sum[l]
    #                 dp[r][k] = min(dp[r][k], max(left, right))

    #     return dp[n - 1][k]

    def splitArray(self, nums: List[int], k: int) -> int:
        # 3.Binary Search, similar problems: 875,1011
        # time complexity: O(N*log N) N=len(nums)
        # space complexity: O(1)

        l, r = max(nums), sum(nums)

        def check(max_sum: int) -> bool:
            cur_sum = 0
            split = 0
            for i in nums:
                if cur_sum + i > max_sum:
                    cur_sum = 0
                    split += 1

                cur_sum += i

            if cur_sum != 0:
                split += 1

            return split <= k

        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1

        return r


# @lc code=end
