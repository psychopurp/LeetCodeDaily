#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     # greedy
    #     # time complexity: O(N)
    #     # space complexity: O(1)
    #     '''
    #     The idea is to iterate backward, keep track of the minimum jump position required.
    #     '''
    #     n = len(nums)
    #     end = n-1
    #     for i in range(n-1, -1, -1):
    #         if nums[i]+i >= end:
    #             end = i
    #     return end == 0

    # def canJump(self, nums: List[int]) -> bool:
    #     # greedy
    #     # time complexity: O(N)
    #     # space complexity: O(1)
    #     '''
    #     iterate forward, keep track of the maximum position that reachable.
    #     '''

    #     n = len(nums)
    #     reachable = 0

    #     for i in range(n):
    #         if i > reachable:
    #             return False
    #         reachable = max(reachable, i+nums[i])
    #     return True

    # def canJump(self, nums: List[int]) -> bool:
    #     # BFS
    #     # time complexity: O(N)
    #     # space complexity: O(N)

    #     from collections import deque

    #     q = deque([0])
    #     visited = set()

    #     while q:
    #         for _ in range(len(q)):
    #             i = q.popleft()
    #             if i+nums[i] >= len(nums)-1:
    #                 return True

    #             for k in range(nums[i]):
    #                 next_pos = i+k+1

    #                 if next_pos not in visited:
    #                     visited.add(next_pos)
    #                     q.append(next_pos)
    #     return False

    # def canJump(self, nums: List[int]) -> bool:
    #     # DFS (Time Limit Exceeded)
    #     # time complexity: O(N)
    #     # space complexity: O(N)

    #     def dfs(cur: int):
    #         nonlocal res

    #         if res:
    #             return

    #         if cur >= len(nums)-1:
    #             res = True
    #             return

    #         for i in range(cur+1, min(len(nums), cur+nums[cur]+1)):
    #             dfs(i)

    #     res = False
    #     dfs(0)
    #     return res

    # def canJump(self, nums: List[int]) -> bool:
    #     # Top down DP : dp[i] represents whether i can reach the end.
    #     # time complexity: O(N^2)
    #     # space complexity: O(N)

    #     n = len(nums)
    #     dp = [False]*n
    #     dp[-1] = True

    #     for i in range(n-2, -1, -1):

    #         for k in range(i+1, min(n, i+nums[i]+1)):
    #             if dp[k]:
    #                 dp[i] = True
    #                 break

    #     return dp[0]

    def canJump(self, nums: List[int]) -> bool:
        # Top down DP (recursive, TLE) : dp[i] represents whether i can reach the end.
        # time complexity: O(N^2)
        # space complexity: O(N)

        def dp(i: int) -> bool:
            if i == len(nums)-1:
                return True

            for k in range(i+1, min(len(nums), i+nums[i]+1)):
                if dp(k):
                    return True

            return False

        return dp(0)

# @lc code=end
