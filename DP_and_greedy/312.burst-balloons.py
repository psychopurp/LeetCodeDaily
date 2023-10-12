#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] Burst Balloons
#

# @lc code=start
from typing import List


class Solution:
    # def maxCoins(self, nums: List[int]) -> int:
    #     # 1. Backtracking, but this will TLE
    #     # time complexity: O(N!)
    #     # space complexity: (N)
    #     from functools import lru_cache

    #     def find_not_burst_ballon_in_range(l: int, r: int, is_right_side: bool) -> int:
    #         res = 1
    #         if l < 0 or r > len(nums) or l > r:
    #             return 1

    #         direction = 1
    #         if not is_right_side:
    #             direction = -1
    #             l, r = r, l - 1
    #         else:
    #             l, r = l, r + 1

    #         for i in range(l, r, direction):
    #             if i not in visited:
    #                 return nums[i]
    #         return res

    #     @lru_cache
    #     def backtrack(cur: int, coins: int):
    #         if len(visited) == len(nums):
    #             nonlocal ans
    #             # print(coins)
    #             ans = max(ans, coins)

    #         for i in range(len(nums)):
    #             if i not in visited:
    #                 visited.add(i)
    #                 l, r = find_not_burst_ballon_in_range(
    #                     0, i - 1, False
    #                 ), find_not_burst_ballon_in_range(i + 1, len(nums) - 1, True)
    #                 backtrack(i, nums[i] * l * r + coins)
    #                 visited.remove(i)

    #     visited = set()
    #     ans = 0
    #     backtrack(0, 0)
    #     return ans

    # def maxCoins(self, nums: List[int]) -> int:
    #     # 2. Top-down DP
    #     # time complexity: O(N^3) N=len(nums) N^2 = Each ballon's state
    #     # space complexity: (N^2)

    #     """
    #     dp[i][j]: represents the maximum coins we can get from range between i to j
    #     """

    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(l: int, r: int) -> int:
    #         coin = 0

    #         # if we burst the Kth ballon at the end, the profit we can make: coin=nums[l] * nums[k] * nums[r] + dp(l, k) + dp(k, r)
    #         for k in range(l + 1, r):
    #             coin = max(coin, nums[l] * nums[k] * nums[r] + dp(l, k) + dp(k, r))
    #         return coin

    #     nums = [1] + nums + [1]

    #     return dp(0, len(nums) - 1)

    def maxCoins(self, nums: List[int]) -> int:
        # 3. Bottom-up DP
        # time complexity: O(N^3) N=len(nums) N^2 = Each ballon's state
        # space complexity: (N^2)

        """
        dp[i][j]: represents the maximum coins we can get from range between i to j

        Explanation: https://leetcode.cn/problems/burst-balloons/solutions/247603/dong-tai-gui-hua-tao-lu-jie-jue-chuo-qi-qiu-wen-ti/
        """

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # Iterate l from bottom to up while iterate r from left to right

        for l in range(n - 1, -1, -1):
            for r in range(l + 1, n):
                for k in range(l + 1, r):
                    dp[l][r] = max(
                        dp[l][r], dp[l][k] + dp[k][r] + nums[k] * nums[l] * nums[r]
                    )

        return dp[0][n - 1]


# @lc code=end
