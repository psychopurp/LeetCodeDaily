#
# @lc app=leetcode.cn id=1884 lang=python3
#
# [1884] Egg Drop With 2 Eggs and N Floors
#


# @lc code=start
class Solution:
    # def twoEggDrop(self, n: int) -> int:
    #     # 1.DP solution
    #     # time complexity: O(N^2*K)
    #     # space complexity: O(N*K)
    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int, k: int) -> int:
    #         if i == 0:
    #             return 0
    #         if k == 1:
    #             return i

    #         min_attempts = float("inf")
    #         for j in range(1, i + 1):
    #             # if egg is broken at j, it will be: dp[j][k] = dp[j-1][k-1] + 1
    #             # if egg is not broken at j, it will be: dp[j][k] = dp[i-j][k] +1
    #             broken = dp(j - 1, k - 1)
    #             not_broken = dp(i - j, k)

    #             # chose the worst case
    #             current_attempts = 1 + max(broken, not_broken)
    #             min_attempts = min(min_attempts, current_attempts)

    #         return min_attempts

    #     return dp(n, 2)

    # def twoEggDrop(self, n: int) -> int:
    #     # 2.DP solution with binary search optimization
    #     # time complexity: O(N^2*K)
    #     # space complexity: O(N*K)
    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int, k: int) -> int:
    #         if i == 0:
    #             return 0
    #         if k == 1:
    #             return i

    #         min_attempts = float("inf")
    #         l, r = 1, i + 1
    #         while l <= r:
    #             # if egg is broken at j, it will be: dp[j][k] = dp[j-1][k-1] + 1
    #             # if egg is not broken at j, it will be: dp[j][k] = dp[i-j][k] +1

    #             j = (l + r) >> 1
    #             broken = dp(j - 1, k - 1)
    #             not_broken = dp(i - j, k)

    #             # chose the worst case
    #             current_attempts = 1 + max(broken, not_broken)
    #             min_attempts = min(min_attempts, current_attempts)

    #             if broken < not_broken:
    #                 l = j + 1
    #             else:
    #                 r = j - 1
    #         return min_attempts

    #     return dp(n, 2)

    def twoEggDrop(self, n: int) -> int:
        # 3.Other DP solution
        # time complexity: O(K*logN)
        # space complexity: O(N*K)

        """
        this DP thinking is different than previous solutions!
        dp[m][k] represents the maximum number of floors that can be "guaranteed" by moving m steps with k eggs.

        explanation for this:
        1. https://leetcode.com/problems/super-egg-drop/solutions/158974/c-java-python-2d-and-1d-dp-o-klogn/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
        """

        from functools import lru_cache

        @lru_cache
        def dp(i: int, k: int) -> int:
            if i == 0:
                return 0
            if k == 1:
                return i

            return 1 + dp(i - 1, k - 1) + dp(i - 1, k)

        for m in range(1, n + 1):
            if dp(m, 2) >= n:
                return m


# @lc code=end
