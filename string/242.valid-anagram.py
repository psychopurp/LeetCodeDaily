#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity: O(n)
        # space complexity: O(n)

        if len(s) != len(t):
            return False

        table = [0]*26

        for i in range(len(s)):
            table[ord(s[i])-ord('a')] += 1
            table[ord(t[i])-ord('a')] -= 1

        for i in table:
            if i != 0:
                return False
        return True
# @lc code=end
