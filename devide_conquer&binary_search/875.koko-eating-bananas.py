#
# @lc app=leetcode.cn id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        # time complexity: O(N*log N)
        # space complexity: O(1)

        l, r = 1, max(piles)

        def check(k: int) -> bool:
            hour = 0

            for i in piles:
                hour += (i + k - 1) // k
                # or
                # hour += i // k
                # if i % k > 0:
                #     hour += 1

            return hour <= h

        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r


# @lc code=end
