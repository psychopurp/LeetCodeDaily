#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        # two-pointers
        # time complexity: O(N) N=len(s)
        # space complexity: O(1)
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# @lc code=end
