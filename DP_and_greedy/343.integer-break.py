#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
from functools import lru_cache


class Solution:
    def integerBreak(self, n: int) -> int:
        # DP
        # time complexity: O(n*n)
        # space complexity: O(n)

        @lru_cache
        def dp(x: int, must_split: bool):
            # must_split 表示这次必须要拆至少两个
            
            if x == 1:
                return 1
            
            # 如果这次不必须拆，可以选择不拆
            if not must_split:
                best = x  # 不拆
            else:
                best = 0  # 必须拆，不能直接用 x

            for i in range(1, x):
                best = max(best, dp(i, False)*dp(x-i, False))

            return best
            
        # 初始必须拆
        return dp(n, True)

# @lc code=end
