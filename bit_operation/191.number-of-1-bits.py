#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] Number of 1 Bits
#


# @lc code=start
class Solution:
    # def hammingWeight(self, n: int) -> int:
    #     # 1.bit operation
    #     # time complexity: O(K) K=32
    #     # space complexity: O(1)

    #     count = 0
    #     while n:
    #         if n & 1:
    #             count += 1
    #         n = n >> 1
    #     return count

    def hammingWeight(self, n: int) -> int:
        # 2.bit operation
        # time complexity: O(log n)
        # space complexity: O(1)

        count = 0
        while n:
            # x & (x-1) => Clear the lowest 1 of x
            # For any number, we can change the lowest 1 of x into 0 if we do x&(x-1).
            n = n & (n - 1)
            count += 1
        return count


# @lc code=end
