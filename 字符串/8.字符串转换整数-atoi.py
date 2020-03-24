#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start

import re


class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)
        num_re = re.findall('^[\+\-]?\d+', str.lstrip())
        num = int(*num_re)
        return max(min(num, INT_MAX), INT_MIN)


# @lc code=end
