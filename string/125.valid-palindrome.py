#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two-pointers
        # time complexity: O(N)
        # space complexity: O(1)
        l, r = 0, len(s) - 1

        while l < r:
            # find letter from left
            while l < r and not s[l].isalnum():
                l += 1

            # find letter from right
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True


# @lc code=end
