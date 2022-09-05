#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    # def jump(self, nums: List[int]) -> int:
    #     # BFS
    #     # time complexity: O(N^2)
    #     # space complexity: O(N)

    #     from collections import deque

    #     q = deque()
    #     q.append((0, 0))
    #     visited = set()

    #     while q:

    #         for _ in range(len(q)):
    #             i, step = q.popleft()
    #             if i == len(nums)-1:[]\[/;=+[]]
    #                 return step

    #             for k in range(i+1, min(len(nums), i+nums[i]+1)):
    #                 if k not in visited:
    #                     visited.add(k)
    #                     q.append((k, step+1))

    # def jump(self, nums: List[int]) -> int:
    #     # DP : dp[i] represents the minimum step for reaching the end.
    #     # time complexity: O(N^2)
    #     # space complexity: O(N)

    #     n = len(nums)
    #     dp = [float("inf")]*n
    #     dp[-1] = 0

    #     for i in range(n-2, -1, -1):

    #         if i+nums[i] >= n-1:
    #             dp[i] = 1
    #             continue

    #         for k in range(i+1, min(n, i+nums[i]+1)):
    #             dp[i] = min(dp[k]+1, dp[i])

    #     return dp[0]

    def jump(self, nums: List[int]) -> int:
        # BFS : consider maxJumpPosition as the current level of BFS
        # time complexity: O(N)
        # space complexity: O(1)

        maxJumpPosition = 0
        i = 0
        n = len(nums)
        step = 0

        while i < n:
            if maxJumpPosition == n-1:
                return step

            curMaxJumpPosition = maxJumpPosition
            step += 1
            while i <= curMaxJumpPosition:
                if i+nums[i] >= len(nums)-1:
                    return step

                maxJumpPosition = max(maxJumpPosition, i+nums[i])
                i += 1

        return step
# @lc code=end
