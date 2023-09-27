#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] Power of Two
#


# @lc code=start
class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     # 1.bit operation
    #     # time complexity: O(1)
    #     # space complexity: O(1)

    #     def get_count_of_1(n: int) -> int:
    #         count = 0
    #         while n:
    #             # x & (x-1) => Clear the lowest 1 of x
    #             # For any number, we can change the lowest 1 of x into 0 if we do x&(x-1).
    #             n = n & (n - 1)
    #             count += 1
    #         return count

    #     if n < 0:
    #         return False

    #     return get_count_of_1(n) == 1

    # def isPowerOfTwo(self, n: int) -> bool:
    #     # 2.bit operation: after clear one 1 bit, it should be 0
    #     # time complexity: O(1)
    #     # space complexity: O(1)

    #     return n > 0 and n & (n - 1) == 0

    def isPowerOfTwo(self, n: int) -> bool:
        # 3.bit operation
        # time complexity: O(1)
        # space complexity: O(1)

        BIG = 1 << 31

        return n > 0 and BIG % n == 0


# @lc code=end
