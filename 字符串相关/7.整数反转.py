#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        return self.reverse_better(x)
        result = []
        flag = True
        if x < 0:
            result.append('-')
        x = str(abs(x))

        for i in x[::-1]:
            if (len(x) == 1 and i == '0') or i != '0':
                flag = False
            if flag:
                continue
            else:
                result.append(i)
        result = int(''.join(result))
        if result > (2 ** 31 - 1) or result < (-2 ** 31):
            result = 0
        return result

    def reverse_better(self, x):
        boundry = (1 << 31) - 1 if x > 0 else (1 << 31)
        y = abs(x)
        result = 0
        while y != 0:
            result = result * 10 + y % 10
            if result > boundry:
                return 0
            y = y // 10
        return result if x > 0 else -result


# @lc code=end
