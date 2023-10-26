#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#


# @lc code=start
from typing import List


class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     # 1.Brute-force: iterate from left to right. This will TLE!
    #     # time complexity: O(N^2)
    #     # space complexity: O(1)

    #     n = len(heights)
    #     max_val = 0

    #     for r in range(n):
    #         min_height = heights[r]
    #         for l in range(r, -1, -1):
    #             min_height = min(min_height, heights[l])
    #             width = r - l + 1
    #             max_val = max(max_val, min_height * width)

    #     return max_val

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     # 2.Brute-force: iterate from down to up. This will TLE!
    #     # time complexity: O(N^2)
    #     # space complexity: O(1)

    #     n = len(heights)
    #     max_val = 0

    #     for i in range(n):
    #         h = heights[i]

    #         # find the left and right boundary
    #         l = r = i
    #         while l >= 0 and heights[l] >= h:
    #             l -= 1

    #         while r < n and heights[r] >= h:
    #             r += 1

    #         max_val = max(max_val, (r - l - 1) * h)

    #     return max_val

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 3.Monotonic stack
        # time complexity: O(N)
        # space complexity: O(N)

        heights.append(0)
        n = len(heights)
        max_val = 0

        stack = []

        for i in range(n):
            r = i
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                l = stack[-1] if stack else -1
                max_val = max(max_val, (r - l - 1) * h)

            stack.append(i)

        return max_val


# @lc code=end
