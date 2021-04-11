#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    # def calculate(self, s: str) -> int:
    #     # 自己最初实现的一版 get_token 可以优化，只遍历一次
    #     def get_token(s) -> []:
    #         token = []
    #         i = 0
    #         while i < len(s):
    #             if s[i] == " ":
    #                 i += 1
    #                 continue

    #             if s[i] in "+-*/":
    #                 token.append(s[i])
    #                 i += 1
    #                 continue
    #             j = i
    #             while i < len(s) and s[i].isdigit():
    #                 i += 1
    #             token.append(s[j:i])
    #         return token

    #     stack = []
    #     operations = {
    #         '+': lambda x, y: x+y,
    #         '-': lambda x, y: x-y,
    #         '*': lambda x, y: x*y,
    #         '/': lambda x, y: int(x/y)
    #     }
    #     token = get_token(s)
    #     cur_tok = ' '
    #     for i in token:
    #         if cur_tok in "*/":
    #             stack.append(operations[cur_tok](stack.pop(), int(i)))
    #         if cur_tok == "+":
    #             stack.append(int(i))
    #         if cur_tok == "-":
    #             stack.append(-int(i))

    #         if cur_tok in "+-*/":
    #             cur_tok = ' '
    #             continue

    #         if i in "+-*/":
    #             cur_tok = i
    #         else:
    #             stack.append(int(i))
    #     return sum(stack)

    def calculate(self, s: str) -> int:
        # 时间复杂度 O(N) 空间复杂度 O(N)

        n = len(s)
        stack = []
        preSign = "+"
        num = 0

        for i in range(n):
            if s[i] != " " and s[i].isdigit():
                num = num*10+ord(s[i])-ord('0')
            if s[i] in "+-*/" or i == n-1:
                if preSign == "+":
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                preSign = s[i]
                num = 0
        return sum(stack)


# @lc code=end
