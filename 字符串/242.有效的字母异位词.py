#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            v1, v2 = s[i], t[i]
            hash[v1] = hash.get(v1, 0) + 1
            hash[v2] = hash.get(v2, 0)-1
        for i in hash:
            if hash[i] != 0:
                return False
        return True
# @lc code=end
