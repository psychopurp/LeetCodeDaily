#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # time complexity: O(n)
        # space complexity: O(1)

        carry = 1
        n = len(digits)-1
        while n+1:
            num = digits[n]+carry
            digits[n] = num % 10
            carry = num // 10
            n -= 1
        if carry:
            digits.insert(0, carry)

        return digits
# @lc code=end
