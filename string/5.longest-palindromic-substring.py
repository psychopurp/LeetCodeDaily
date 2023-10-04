#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] Longest Palindromic Substring
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 1.From middle to two ends
        # time complexity: O(N^2)
        # space complexity: O(1)

        # get the longest palindrome, l, r are the middle indexes
        # from inner to outer
        def expandAroundCenter(l: int, r: int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        start = end = 0
        for i in range(len(s)):
            # odd case like "aba"
            l1, r1 = expandAroundCenter(i, i)
            # even case like "abba"
            l2, r2 = expandAroundCenter(i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2
        return s[start : end + 1]


# @lc code=end
