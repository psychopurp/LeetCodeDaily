#
# @lc app=leetcode.cn id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from functools import lru_cache


class Solution:
    # def numSquares(self, n: int) -> int:
    #     # Bottom-up DP
    #     # time complexity: O(n*sqrt(n))
    #     # space complexity: O(n)

    #     dp = [0]*(n+1)

    #     for i in range(1, n+1):
    #         # the worst case
    #         dp[i] = i

    #         for j in range(1, n+1):
    #             if j*j > i:
    #                 break

    #             dp[i] = min(dp[i], dp[i-j*j]+1)

    #     return dp[-1]

    # def numSquares(self, n: int) -> int:
    #     # Top-down dp
    #     # time complexity: O(n*sqrt(n))
    #     # space complexity: O(n)

    #     @lru_cache(None)
    #     def dp(i: int) -> int:
    #         val = i
    #         for j in range(1, n+1):
    #             if j*j > i:
    #                 break
    #             val = min(val, dp(i-j*j)+1)
    #         return val

    #     return dp(n)

    # def numSquares(self, n: int) -> int:
    #     # BFS
    #     # time complexity: O(n*sqrt(n))
    #     # space complexity: O(n)

    #     from collections import deque

    #     visited = set()
    #     q = deque()
    #     q.append((0, 1))

    #     while q:
    #         for _ in range(len(q)):
    #             u, depth = q.popleft()
    #             for i in range(1, n+1):
    #                 v = u+i*i
    #                 if v == n:
    #                     return depth

    #                 if v > n:
    #                     break

    #                 if v not in visited:
    #                     visited.add(v)
    #                     q.append((v, depth+1))

    def numSquares(self, n: int) -> int:
        # Bottom-up DP, same as coin change
        # time complexity: O(n*sqrt(n))
        # space complexity: O(n)

        nums = []
        for i in range(n + 1):
            if i * i > n:
                break
            nums.append(i * i)

        dp = [i for i in range(n + 1)]

        for i in range(n + 1):
            for num in nums:
                if i + num <= n:
                    dp[i + num] = min(dp[i + num], dp[i] + 1)
        return dp[-1]


# @lc code=end
