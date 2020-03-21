#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)):
            tmp = haystack[i:i+len(needle)]
            if tmp == needle:
                return i
            if i + len(needle) < len(haystack) and haystack[i + len(needle)] not in needle:
                i = i + len(needle)
        return -1
# @lc code=end


def strStr(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        tmp = haystack[i:i+len(needle)]
        if tmp == needle:
            return i
        if i + len(needle) < len(haystack) and haystack[i + len(needle)] not in needle:
            i = i + len(needle)
    return -1


a = "hello"
b = "ll"
print(strStr(a, b))
# print('a'.index(''))
