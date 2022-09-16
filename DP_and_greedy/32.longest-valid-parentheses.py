#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    #     # stack: mark the positions where the braces are valid and then calculate the longest valid
    #     # time complexity: O(N)
    #     # space complexity: O(N)

    #     n = len(s)
    #     stack = []
    #     valid = [False]*n

    #     for i in range(n):
    #         if s[i] == "(":
    #             stack.append(i)
    #         else:
    #             if stack:
    #                 valid[stack.pop()] = valid[i] = True

    #     max_val = 0
    #     count = 0
    #     for v in valid:
    #         if v:
    #             count += 1
    #         else:
    #             count = 0
    #         max_val = max(max_val, count)

    #     return max_val

    # def longestValidParentheses(self, s: str) -> int:
    #     # stack: eliminate every valid braces and then calculate the distance of adjacent invalid index
    #     # time complexity: O(N)
    #     # space complexity: O(N)

    #     n = len(s)
    #     stack = [-1]
    #     max_val = 0

    #     for i in range(n):
    #         if len(stack) > 1 and s[i] == ")" and s[stack[-1]] == "(":
    #             stack.pop()
    #             max_val = max(max_val, i-stack[-1])
    #         else:
    #             stack.append(i)

    #     return max_val

    def longestValidParentheses(self, s: str) -> int:
        # Bottom-up DP : dp[i] represents the longest valid braces ending with i
        # time complexity: O(N)
        # space complexity: O(N)

        n = len(s)
        dp = [0]*(n+1)

        for i in range(1, n):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2]+2
                elif s[i-1] == ")":
                    prev_i = i-dp[i-1]-1
                    if prev_i >= 0 and s[prev_i] == "(":
                        dp[i] = dp[prev_i-1]+dp[i-1]+2

        return max(dp)


# @lc code=end
