#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from typing import List


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     n = len(nums)
    #     L, R, ans = [0]*n, [0]*n, [0]*n
    #     L[0], R[n-1] = 1, 1

    #     for i in range(n):
    #         leftIndex = i
    #         rightIndex = n-1-i

    #         if leftIndex > 0:
    #             L[leftIndex] = L[leftIndex-1]*nums[leftIndex-1]

    #         if rightIndex < n-1:
    #             R[rightIndex] = R[rightIndex+1]*nums[rightIndex+1]

    #     for i in range(n):
    #         ans[i] = L[i]*R[i]

    #     return ans

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # optimize the previous solution
        # time complexity: O(n)
        # space complexity: O(1)

        n = len(nums)
        ans = [1]
        L, R, = 1, 1

        for i in range(n-1):
            L *= nums[i]
            ans.append(L)

        for i in range(n-1, 0, -1):
            R *= nums[i]
            ans[i-1] *= R

        return ans


# @lc code=end
