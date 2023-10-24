#
# @lc app=leetcode.cn id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # binary select
        # time complexity: O(N*log N)
        # space complexity: O(1)

        l, r = max(weights), sum(weights)

        def feasible(capacity: int) -> bool:
            day = 0
            cur_load = 0

            for i in weights:
                if cur_load + i > capacity:
                    cur_load = 0
                    day += 1

                cur_load += i

            if cur_load != 0:
                day += 1

            return day <= days

        while l < r:
            mid = (l + r) >> 1
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return r


# @lc code=end
