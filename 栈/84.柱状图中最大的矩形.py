#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

# @lc code=start


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # 时间复杂度O(N) 空间复杂度 O(N)
        stack = []
        area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = stack.pop()
                left = stack[-1] if stack else - 1
                area = max(area, heights[height]*(i-left-1))

            stack.append(i)
        return area


# @lc code=end
