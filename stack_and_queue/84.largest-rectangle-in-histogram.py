#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     # brute force solution 1
    #     # time complexity: O(n^2)
    #     # space complexity: O(1)
    #     maxArea = 0
    #     for i in range(len(heights)):
    #         minHeight = heights[i]
    #         for j in range(i, len(heights)):
    #             minHeight = min(minHeight, heights[j])
    #             maxArea = max(maxArea, (j+1-i)*minHeight)
    #     return maxArea

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     # brute force solution 2
    #     # time complexity: O(n^2)
    #     # space complexity: O(1)

    #     maxArea = 0
    #     for i in range(len(heights)):
    #         curHeight = heights[i]

    #         # find left boundary
    #         left = i
    #         while left-1 >= 0 and heights[left-1] >= curHeight:
    #             left -= 1

    #         # find right boundary
    #         right = i
    #         while right+1 < len(heights) and heights[right+1] >= curHeight:
    #             right += 1
    #         maxArea = max(maxArea, (right-left+1)*curHeight)
    #     return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        # Monotone stack solution
        # time complexity: O(n)
        # space complexity: O(n)
        maxArea = 0
        heights.append(0)
        stack = []

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                curHeight = heights[stack.pop()]
                right = i
                left = stack[-1] if stack else -1
                maxArea = max(maxArea, (right-left-1)*curHeight)

            stack.append(i)

        return maxArea

# @lc code=end
