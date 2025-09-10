#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
from functools import lru_cache


class Solution:

    # @lru_cache
    # def fib(self, n: int) -> int:
    #     # recursion solution
    #     # time complexity: O(n)
    #     # space complexity: O(n)
    #     if n<=1:
    #         return n

    #     return self.fib(n-1)+self.fib(n-2)

    def fib(self, n: int) -> int:
        # Bottom-up DP
        # time complexity: O(n)
        # space complexity: O(1)

        if n <= 1:
            return n
        n_2, n_1 = 0, 1
        for _ in range(n-1):
            n_2, n_1 = n_1, n_1+n_2

        return n_1


# @lc code=end
