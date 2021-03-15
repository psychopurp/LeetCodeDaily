#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # 使用栈 空间复杂度O(N) 时间复杂度O(N)
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i-stack[-1])
        return max_len

    # def longestValidParentheses(self, s: str) -> int:
    #     # dp[i] 表示以i结尾的最长有效括号 空间复杂度O(N) 时间复杂度O(N)
    #     dp = [0]*len(s)
    #     res = 0
    #     for i in range(len(s)):
    #         if s[i] == ")":
    #             if i > 0 and s[i-1] == "(":
    #                 dp[i] = dp[i-2]+2
    #             elif i-dp[i-1]-1 >= 0 and s[i-1] == ")" and s[i-dp[i-1]-1] == "(":
    #                 dp[i] = dp[i-1]+2+dp[i-dp[i-1]-2]
    #             res = max(res, dp[i])
    #     return res

    # def longestValidParentheses(self, s: str) -> int:
    #     # 暴力解法 时间复杂度O(N*3) 空间复杂度O(N)
    #     def isValid(s):
    #         stack = []
    #         for i in s:
    #             if i == "(":
    #                 stack.append(i)
    #             elif stack and stack[-1] == "(":
    #                 stack.pop()
    #             else:
    #                 return False
    #         return len(stack) == 0
    #     for i in range(len(s), -1, -1):
    #         for j in range(len(s)-i+1):
    #             if isValid(s[j:i+j]):
    #                 return i
    #     return 0

        # @lc code=end
