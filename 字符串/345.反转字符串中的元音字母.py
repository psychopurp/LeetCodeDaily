#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
        low, high = 0, len(s) - 1
        s = list(s)
        while low < high:
            if s[low] not in vowels:
                low += 1
                continue
            if s[high] not in vowels:
                high -= 1
                continue
            else:
                s[low], s[high] = s[high], s[low]
                low += 1
                high -= 1
        return "".join(s)


# @lc code=end
