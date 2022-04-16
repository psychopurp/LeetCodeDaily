#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    # def letterCombinations(self, digits: str) -> List[str]:
    #     # iterative way with brute force
    #     # space complexity: O(m+n)
    #     # time complexity: O(3^m * 4^n)
    #     phone = {
    #         "2": "abc",
    #         "3": "def",
    #         "4": "ghi",
    #         "5": "jkl",
    #         "6": "mno",
    #         "7": "pqrs",
    #         "8": "tuv",
    #         "9": "wxyz"
    #     }

    #     ans = []
    #     for digit in digits:
    #         if not ans:
    #             ans.extend(phone[digit])
    #             continue

    #         newSubset = []
    #         for c in phone[digit]:
    #             for subset in ans:
    #                 newSubset.append(subset+c)
    #         ans = newSubset

    #     return ans

    # def letterCombinations(self, digits: str) -> List[str]:
    #     # backtracking
    #     # space complexity: O(m+n)
    #     # time complexity: O(3^m * 4^n)
    #     phone = {
    #         "2": "abc",
    #         "3": "def",
    #         "4": "ghi",
    #         "5": "jkl",
    #         "6": "mno",
    #         "7": "pqrs",
    #         "8": "tuv",
    #         "9": "wxyz"
    #     }

    #     def backtrack(way: List[str], index: int):

    #         if index == len(digits):
    #             if way:
    #                 ans.append("".join(way))
    #             return

    #         for c in phone[digits[index]]:
    #             way.append(c)
    #             backtrack(way, index+1)
    #             way.pop()

    #     ans = []
    #     backtrack([], 0)
    #     return ans

    def letterCombinations(self, digits: str) -> List[str]:
        # iterative way with queue
        # space complexity: O(m+n)
        # time complexity: O(3^m * 4^n)

        from collections import deque

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if not digits:
            return []

        q = deque()
        q.append("")

        while q and len(q[0]) != len(digits):
            tmp = q.popleft()

            charSet = phone[digits[len(tmp)]]

            for c in charSet:
                q.append(tmp+c)

        return list(q)
# @lc code=end
