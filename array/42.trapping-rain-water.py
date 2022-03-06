#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
from typing import List


class Solution:
    # def trap(self, height: List[int]) -> int:
    #     # monotonic stack solution
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     stack = []
    #     ans = 0
    #     for i in range(len(height)):
    #         if stack and height[i] > height[stack[-1]]:
    #             # pop process
    #             while stack and height[i] > height[stack[-1]]:
    #                 mid = stack.pop()
    #                 if not stack:
    #                     stack.append(i)
    #                     break

    #                 w = i - stack[-1]-1
    #                 h = min(height[i], height[stack[-1]]) - height[mid]
    #                 ans += w*h
    #         else:
    #             stack.append(i)

    #     return ans

    # def trap(self, height: List[int]) -> int:
    #     # dp solution
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     n = len(height)
    #     ans = 0
    #     maxLeft, maxRight = [0]*n, [0]*n

    #     for i in range(n):
    #         if i > 0:
    #             maxLeft[i] = max(maxLeft[i-1], height[i-1])
    #             maxRight[n-i-1] = max(maxRight[n-i], height[n-i])

    #     for i in range(n):
    #         minHeight = min(maxLeft[i], maxRight[i])
    #         if minHeight > height[i]:
    #             ans += minHeight-height[i]

    #     return ans

    def trap(self, height: List[int]) -> int:
        # dp solution with two-pointer optimization
        # time complexity: O(n)
        # space complexity: O(1)

        leftCursor, rightCursor = 0, len(height)-1
        leftMax, rightMax, ans = 0, 0, 0

        while leftCursor <= rightCursor:
            leftMax = max(leftMax, height[leftCursor])
            rightMax = max(rightMax, height[rightCursor])

            if leftMax < rightMax:
                ans += leftMax-height[leftCursor]
                leftCursor += 1
            else:
                ans += rightMax-height[rightCursor]
                rightCursor -= 1

        return ans

# @lc code=end
