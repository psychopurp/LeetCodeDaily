#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
from typing import List


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # two-poniters
        # time complexity: O(N)
        # space complexity: O(N) N=len(s) Depends on the nature of the string type in the language used. If the string is mutable, then we can modify it directly on the original string with a space complexity of O (1), otherwise we need to use O (n) to temporarily convert the string into a data structure that can be modified.
        def reverse(s: List[str], left: int, right: int):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

        s_list = list(s)
        n = len(s)
        left = 0

        while left < n:
            right = left + k - 1
            reverse(s_list, left, min(right, n - 1))
            left = left + 2 * k
        return "".join(s_list)


# @lc code=end
