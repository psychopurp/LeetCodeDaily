#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Vertical scanning
        # time complexity: O(M*N) M=len(strs) N=min(strs[0])
        # spcae complexity: O(N)

        n = len(strs[0])

        for i in range(n):
            tmp_val = ""
            for word in strs:
                if not tmp_val:
                    tmp_val = word[i]
                elif i >= len(word) or word[i] != tmp_val:
                    return word[:i]

        return strs[0]


# @lc code=end
