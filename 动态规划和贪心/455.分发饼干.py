#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        s.sort()
        g.sort()
        j = 0
        for x in g:
            while j < len(s) and s[j] < x:
                j += 1
            if j < len(s):
                count += 1
                j += 1
        return count


# @lc code=end
