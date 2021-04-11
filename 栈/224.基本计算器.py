#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
class Solution:
    # def calculate(self, s: str) -> int:
    #     # 自己的初版实现 首先去除括号，之后通过栈来计算
    #     preSign = "+"
    #     n = len(s)
    #     bracket = []
    #     token = []

    #     num = 0
    #     i = 0
    #     while i < n:
    #         if s[i] == " ":
    #             i += 1
    #             continue
    #         if s[i] == "(":
    #             bracket.append(preSign)
    #             i += 1
    #             continue

    #         if s[i] == ")":
    #             bracket.pop()
    #             i += 1
    #             continue

    #         if s[i] in "+-*/":
    #             preSign = s[i]
    #             if bracket and bracket[-1] == "-":
    #                 if s[i] == "+":
    #                     token.append("-")
    #                     preSign = "-"
    #                 elif s[i] == "-":
    #                     token.append("+")
    #                     preSign = "+"
    #             else:
    #                 token.append(s[i])

    #             i += 1
    #             continue

    #         while i < n and s[i].isdigit():
    #             num = num*10+ord(s[i])-ord(("0"))
    #             i += 1
    #         token.append(str(num))
    #         num = 0

    #     preSign = "+"
    #     stack = []
    #     for i in token:
    #         if i.isdigit():
    #             if preSign == "-":
    #                 stack.append(-int(i))
    #             elif preSign == "+":
    #                 stack.append(int(i))
    #             elif preSign == "*":
    #                 stack.append(stack.pop()*int(i))
    #             elif preSign == "/":
    #                 stack.append(int(stack.pop()/int(i)))
    #         else:
    #             preSign = i
    #     return sum(stack)

    # def calculate(self, s: str) -> int:
    #     '''
    #     使用栈来递归
    #     s = "1 + (3 - (4 + 5+1))"

    #     1: left=1 sign:+
    #     2: left=1 sign:+ stack=[1,+]
    #     3: left=3 sign:-
    #     4: left=3 sign:- stack=[1,+,3,-]
    #     5: left=4 sign:+
    #     6: left=9 sign:+
    #     7: left=9 sign:+ num=1 stack=[1,+,3,-]
    #     8: left=10 -> -7  sign:+ num=0 stack=[1,+,3,-] -> [1,+]
    #     9: left=-7 -> -6 sign:+ num=0 stack[1,+] -> []
    #     '''
    #     left = 0
    #     num = 0
    #     sign = 1
    #     stack = []

    #     for c in s:

    #         if c.isdigit():
    #             num = num*10+int(c)
    #         elif c in "+-":
    #             left += num*sign
    #             num = 0
    #             sign = 1 if c == "+" else -1
    #         elif c == "(":
    #             stack.append(left)
    #             stack.append(sign)
    #             left = 0
    #             sign = 1
    #         elif c == ")":
    #             left += num*sign
    #             num = 0
    #             left *= stack.pop()
    #             left += stack.pop()
    #     left += num*sign
    #     return left

    def calculate(self, s: str) -> int:
        def dfs(s: str):
            nonlocal i, n
            num = 0
            res = 0
            sign = 1

            while i < n:
                if s[i] == " ":
                    i += 1
                    continue

                if s[i].isdigit():
                    num = num*10+int(s[i])
                    i += 1
                    continue

                if s[i] in "+-":
                    res += sign*num
                    num = 0
                    sign = 1 if s[i] == "+" else -1
                    i += 1
                    continue

                if s[i] == "(":
                    i += 1
                    res += dfs(s)*sign
                    continue

                if s[i] == ")":
                    res += sign*num
                    num = 0
                    i += 1
                    return res
            res += sign*num
            return res

        i = 0
        n = len(s)
        return dfs(s)

# @lc code=end
