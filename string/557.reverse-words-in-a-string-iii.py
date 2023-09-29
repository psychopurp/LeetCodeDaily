#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] Reverse Words in a String III
#


# @lc code=start
from typing import List


class Solution:
    def reverseWords(self, s: str) -> str:
        # two-pointers
        # time complexity: O(N) N=len(s)
        # space complexity: O(N) used in s_list

        def reverse(s: List[str], left: int, right: int):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        s_list = list(s)
        right = -1

        n = len(s)
        i = 0
        while i < n:
            left = i

            while i < n and s[i] != " ":
                i += 1

            right = i - 1
            reverse(s_list, left, right)

            while i < n and s[i] == " ":
                i += 1

        return "".join(s_list)


# @lc code=end
