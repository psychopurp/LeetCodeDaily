#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # greedy solution
        # time complexity: O(mlogm+nlogn)
        # space complexity: O(logm+logn) used in sorting

        g.sort()
        s.sort()

        children = 0

        for cookie in s:
            if children == len(g):
                break

            if g[children] <= cookie:
                children += 1

        return children
# @lc code=end
