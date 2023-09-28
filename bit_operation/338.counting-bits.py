#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
from typing import List


class Solution:
    # def countBits(self, n: int) -> List[int]:
    #     # 1.bit operation
    #     # time complexity: O(n*log n)
    #     # space complexity: O(1)
    #     def get_count_of_1(n: int) -> int:
    #         count = 0
    #         while n:
    #             n = n & (n - 1)
    #             count += 1
    #         return count

    #     return [get_count_of_1(i) for i in range(n + 1)]

    def countBits(self, n: int) -> List[int]:
        # 2.bit operation with DP: https://leetcode.cn/problems/counting-bits/solutions/7882/hen-qing-xi-de-si-lu-by-duadua/
        # time complexity: O(n*log n)
        # space complexity: O(1)

        dp = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            # it can by divided by 2
            if i & 1 == 0:
                dp[i] = dp[i >> 1]
            else:
                dp[i] = dp[i - 1] + 1

        return dp


# @lc code=end
