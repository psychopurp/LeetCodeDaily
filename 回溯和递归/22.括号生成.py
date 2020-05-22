#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(left, right, n, track):
            if left == n and right == n:
                ways.append(track)
                return
            if left < n:
                backtrack(left + 1, right, n, track + '(')
            if left > right:
                backtrack(left, right + 1, n, track + ')')

        ways = []
        backtrack(0, 0, n, '')
        return ways


# @lc code=end
