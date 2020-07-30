#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start


class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     low, high = 0, len(s) - 1
    #     gap = ord('a')-ord('A')
    #     while low < high:
    #         if not self.check(s[low]):
    #             low += 1
    #             continue
    #         if not self.check(s[high]):
    #             high -= 1
    #             continue
    #         if (('0' <= s[low] <= '9') and (s[high] > '9' or s[high] < '0')) or (('0' <= s[high] <= '9') and (s[low] > '9' or s[low] < '0')):
    #             return False
    #         if s[low] == s[high] or (ord(s[low]) + gap) == ord(s[high]) or (ord(s[low]) - gap) == ord(s[high]):
    #             low += 1
    #             high -= 1
    #         else:
    #             return False
    #     return True

    def isPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1

        while low < high:
            if not s[low].isalnum():
                low += 1
                continue
            if not s[high].isalnum():
                high -= 1
                continue
            if s[low].lower() != s[high].lower():
                return False
            low += 1
            high -= 1
        return True

    def check(self, char):
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9'):
            return True
        else:
            return False

# @lc code=end
