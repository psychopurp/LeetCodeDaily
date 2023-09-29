#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] Reverse Only Letters
#


# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # two-pointers
        # time complexity: O(N) N=len(s)
        # space complexity: O(1)
        s_list = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalpha():
                left += 1
            while left < right and not s[right].isalpha():
                right -= 1

            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

        return "".join(s_list)


# @lc code=end
