#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    # def reverseBits(self, n: int) -> int:
    #     # 分治合并
    #     n = (n >> 16) | (n << 16)  # 左边16位移到右边，右边16位移到左边
    #     n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
    #     n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
    #     n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
    #     n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    #     return n

    # def reverseBits(self, n: int) -> int:
    #     # 取模求和
    #     ans = 0
    #     for i in range(32):
    #         ans = (ans << 1) | (n & 1)
    #         n = n >> 1
    #     return ans

    # def reverseBits(self, n: int) -> int:
    #     # 变成字符串转换
    #     y = bin(n)[2:].zfill(32)
    #     return int(y[::-1], 2)

    def reverseBits(self, n: int) -> int:
        # 按位翻转
        ans = 0
        for i in range(32):
            mask = 1 << i
            mask = 1 << (31 - i) if (mask & n) != 0 else 0  # 判断对应的位是0还是1
            ans |= mask
        return ans


# @lc code=end
