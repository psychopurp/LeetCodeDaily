#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:

    # def maxArea(self, height: List[int]) -> int:
    #     # brute force
    #     # time complexity O(n^2)
    #     # space complexity O(1)
    #     n = len(height)
    #     area = 0
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             area = max(area, min(height[i], height[j]) * (j - i), area)
    #     return area

    def maxArea(self, height: List[int]) -> int:
        # 双指针法 时间复杂度 O(n)
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max(min(height[left], height[right]) * (right - left), area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area


# @lc code=end
