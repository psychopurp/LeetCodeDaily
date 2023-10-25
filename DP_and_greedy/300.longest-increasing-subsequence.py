#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start

from typing import List


class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     # Bottom-up DP : dp[i] represents longest increasing subsequence ending with i
    #     # time complexity: O(N^2)
    #     # space complexity: O(N)

    #     n = len(nums)
    #     dp = [1]*n
    #     max_val = 1

    #     for i in range(n):

    #         for k in range(i):
    #             if nums[i] > nums[k]:
    #                 dp[i] = max(dp[i], dp[k]+1)
    #                 max_val = max(max_val, dp[i])
    #     return max_val

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     # Top-down DP : dp[i] represents longest increasing subsequence ending with i
    #     # time complexity: O(N^2)
    #     # space complexity: O(N)

    #     @lru_cache(None)
    #     def dp(i: int) -> int:
    #         nonlocal res
    #         max_val = 1

    #         for k in range(i-1, -1, -1):
    #             if nums[i] > nums[k]:
    #                 max_val = max(max_val, dp(k)+1)
    #                 res = max(res, max_val)
    #         return max_val

    #     res = 1
    #     for i in range(len(nums)-1, -1, -1):
    #         dp(i)
    #     return res

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     # Top-down DP : greedy with binary search : https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
    #     # time complexity: O(N * log N)
    #     # space complexity: O(N) we can achieve O(1) in space by overwriting values of sub into original nums array.

    #     def binary_search(nums: List[int], target: int) -> int:
    #         l, r = 0, len(nums)-1

    #         while l <= r:
    #             mid = (l+r)//2
    #             if target > nums[mid]:
    #                 l = mid+1
    #             else:
    #                 r = mid-1
    #         return l
    #     sub = []

    #     for x in nums:
    #         if not sub or x > sub[-1]:
    #             sub.append(x)
    #         else:
    #             # Find the index of the smallest number
    #             # can be optimized to O(log N) by using binary search
    #             i = binary_search(sub, x)
    #             sub[i] = x

    #     return len(sub)

    def lengthOfLIS(self, nums: List[int]) -> int:
        # Bottom-up DP
        # time complexity: O(N^2)
        # space complexity: O(N)

        """
        dp[i][0] represents the when not select nums[i], the longest subsequence of the array till i.
        dp[i][1] represents the when select nums[i], the longest subsequence of the array till i.
        """

        n = len(nums)
        dp = [[0, 1] for _ in range(n)]

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] > nums[j]:
                    dp[i][1] = max(dp[i][1], dp[j][1] + 1)

            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])

        return max(dp[n - 1][1], dp[n - 1][0])


# @lc code=end
