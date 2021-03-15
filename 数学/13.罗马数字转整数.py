#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    # def romanToInt(self, s: str) -> int:
    #     # 使用栈 时间复杂度O(n),空间复杂度O(n)
    #     table = {"I": 1, "V": 5, "X": 10, "L": 50,
    #              "C": 100, "D": 500, "M": 1000}
    #     total = 0
    #     stack = []
    #     for i in range(len(s)):
    #         val = s[len(s) - i - 1]

    #         if not stack:
    #             total += table[val]
    #         elif table[stack[-1]] <= table[val]:
    #             total += table[val]
    #         else:
    #             total -= table[val]
    #         stack.append(val)
    #     return total

    def romanToInt(self, s: str) -> int:
        # 时间复杂度O(n),空间复杂度O(1)
        table = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
        total = 0
        for i in range(len(s)):

            if i < len(s) - 1:
                if table[s[i]] >= table[s[i + 1]]:
                    total += table[s[i]]
                else:
                    total -= table[s[i]]
            else:
                total += table[s[i]]

        return total


# @lc code=end
