#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash = {}
        for i in s:
            hash[i] = hash.get(i, 0)+1
        for i in hash:
            if hash[i] == 1:
                return s.find(i)
        return -1

# @lc code=end
