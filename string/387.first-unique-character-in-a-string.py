#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Hash
        # time complexity: O(2*N) N=len(s)
        # space complexity: O(N)
        hash = {}
        for i in range(len(s)):
            if s[i] not in hash:
                hash[s[i]] = i
            else:
                hash[s[i]] = -1

        min_val = -1
        for key in hash:
            val = hash[key]
            if val != -1:
                if min_val == -1:
                    min_val = val
                else:
                    min_val = min(min_val, val)
        return min_val


# @lc code=end
