#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     total = 0
    #     for i in range(32):
    #         if n & 1 != 0:
    #             total += 1
    #         n = n >> 1
    #     return total

    # def hammingWeight(self, n: int) -> int:
    #     # 对于任意一个数，将 n 和 n-1 进行 & 运算，我们都可以把 n 中最低位的 1 变成 0
    #     total = 0
    #     while n > 0:
    #         n &= n - 1
    #         total += 1
    #     return total

    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            if n & 1:
                total += 1
            n >>= 1
        return total

# @lc code=end
