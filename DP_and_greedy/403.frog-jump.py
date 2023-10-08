#
# @lc app=leetcode.cn id=403 lang=python3
#
# [403] Frog Jump
#

# @lc code=start
from typing import List


class Solution:
    # def canCross(self, stones: List[int]) -> bool:
    #     # 1.DFS with memorization
    #     # time complexity: O(N^2) without memorization the time complexity will be O(3^n)
    #     # space complexity: O(N^2)
    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int, k: int) -> bool:
    #         if i == len(stones) - 1:
    #             return True

    #         for next_step in [k, k + 1, k - 1]:
    #             if next_step <= 0:
    #                 continue

    #             for j in range(i + 1, len(stones)):
    #                 # next point we can jump
    #                 if stones[i] + next_step == stones[j]:
    #                     if dp(j, next_step):
    #                         return True
    #                 elif stones[i] + next_step < stones[j]:
    #                     break

    #         return False

    #     return dp(0, 0)

    # def canCross(self, stones: List[int]) -> bool:
    #     # 2.DFS with memorization
    #     # time complexity: O(N^2)
    #     # space complexity: O(N^2)
    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int, k: int) -> bool:
    #         if i == len(stones) - 1:
    #             return True

    #         for j in range(i + 1, len(stones)):
    #             diff = stones[j] - stones[i]
    #             if k - 1 <= diff <= k + 1 and diff > 0 and dp(j, diff):
    #                 return True

    #             elif diff > k + 1:
    #                 break
    #         return False

    #     return dp(0, 0)

    # def canCross(self, stones: List[int]) -> bool:
    #     # 3.Bottom-up DP
    #     # time complexity: O(N^2)
    #     # space complexity: O(N^2)

    #     """
    #     dp[i][k]: whether can jump to i from j by k units
    #     dp[i][k]=dp[j][k-1] || dp[j][k] || dp[j][k+1]
    #     """

    #     n = len(stones)
    #     dp = [[False for _ in range(n)] for _ in range(n)]
    #     dp[0][0] = True

    #     for i in range(1, n):
    #         for j in range(i - 1, -1, -1):
    #             k = stones[i] - stones[j]
    #             if k > j + 1:
    #                 break

    #             dp[i][k] = dp[j][k - 1] or dp[j][k] or dp[j][k + 1]
    #             if i == n - 1 and dp[i][k]:
    #                 return True
    #     return False

    def canCross(self, stones: List[int]) -> bool:
        # 4.BFS
        # time complexity: O(N^2)
        # space complexity: O(N^2)

        from collections import deque

        q = deque()
        visited = set()
        n = len(stones)
        q.append((stones[0], 0))
        visited.add((stones[0], 0))

        while q:
            i, k = q.popleft()
            if i == n - 1:
                return True

            for j in range(i + 1, n):
                diff = stones[j] - stones[i]
                if diff > k + 1:
                    break

                if k - 1 <= diff <= k + 1 and diff > 0 and (j, diff) not in visited:
                    visited.add((j, diff))
                    q.append((j, diff))
        return False


# @lc code=end
