#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] Isomorphic Strings
#


# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Hash
        # time complexity: O(N) N=len(s)=len(t)
        # space compelxity: O(2*N)

        n = len(s)
        table = {}
        used = set()
        for i in range(n):
            if s[i] not in table and t[i] not in used:
                table[s[i]] = t[i]
                used.add(t[i])

            if table.get(s[i], "") != t[i]:
                return False

        return True


# @lc code=end
