#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    # def myPow(self, x: float, n: int) -> float:
    #     # brute force solution
    #     # time complexity: O(n)
    #     # space complexity: O(1)

    #     ans = 1
    #     for _ in range(abs(n)):
    #         if n < 0:
    #             ans /= x
    #         else:
    #             ans *= x

    #     return ans

    # def myPow(self, x: float, n: int) -> float:
    #     # devide and conquer
    #     # time complexity: O(logN)
    #     # space complexity: O(logN)

    #     if n == 0:
    #         return 1.0

    #     if n < 0:
    #         n = -n
    #         x = 1/x

    #     ret = self.myPow(x, n//2)
    #     return ret*ret if n % 2 == 0 else ret*ret*x

    def myPow(self, x: float, n: int) -> float:
        # iterative way with Binary Exponentiation
        # time complexity: O(logN)
        # space complexity: O(1)

        if n == 0:
            return 1.0

        if n < 0:
            x = 1/x
            n = -n

        ans = 1
        while n > 0:
            # odd
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans

# @lc code=end
