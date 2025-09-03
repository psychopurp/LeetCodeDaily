#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # solution 1: greedy
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        result = []

        left, right = newInterval
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < left:
            l, r = intervals[i]
            result.append([l, r])
            i += 1

        while i < n and (intervals[i][1] <= left or intervals[i][0] <= right):
            l, r = intervals[i]
            left = min(left, l)
            right = max(right, r)
            i += 1

        result.append([left, right])

        while i < n:
            l, r = intervals[i]
            result.append([l, r])
            i += 1

        return result

# @lc code=end
