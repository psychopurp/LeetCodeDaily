#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 时间复杂度O(log N)
        if n == 0:
            return 1.0
        if n < 0:
            x = 1 / x
            n = abs(n)
        sub = self.myPow(x, n // 2)
        if n % 2 == 0:
            return sub * sub
        else:
            return sub*sub*x


# @lc code=end
