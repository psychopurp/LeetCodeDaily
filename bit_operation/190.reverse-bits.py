#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] Reverse Bits
#


# @lc code=start
class Solution:
    # def reverseBits(self, n: int) -> int:
    #     # 1. bit operation
    #     # time complexity: O(1)
    #     # space complexity: O(1)
    #     ret = 0
    #     for i in range(32):
    #         # check whether i is one, if so then mark (31-i) position to one
    #         mask = (1 << i) & n
    #         if mask:
    #             ret |= 1 << (31 - i)

    #     return ret

    def reverseBits(self, n: int) -> int:
        # 2. bit operation: In each step, we move ret to left while move n to right.
        # time complexity: O(1)
        # space complexity: O(1)

        ret = 0
        for i in range(32):
            ret <<= 1
            ret |= n & 1
            n >>= 1
        return ret


# @lc code=end
