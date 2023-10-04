#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] Valid Palindrome II
#


# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two-pointers with simple backtracking
        # time complexity: O(N)
        # space complexity: O(1)
        def verify(l: int, r: int, deleted: bool) -> bool:
            while l < r:
                if s[l] != s[r]:
                    if deleted:
                        return False

                    return verify(l + 1, r, True) or verify(l, r - 1, True)
                else:
                    l += 1
                    r -= 1
            return True

        return verify(0, len(s) - 1, False)


# @lc code=end
