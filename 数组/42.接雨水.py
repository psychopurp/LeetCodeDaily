#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start


class Solution:
    # def trap(self, height: List[int]) -> int:
    #     # 时间复杂度O(n*2)
    #     # 空间复杂度O(1)
    #     def find_next_big(nums, i, left=False):
    #         # val = nums[i]
    #         if left:
    #             next_big = max(nums[:i])
    #             return next_big
    #         else:
    #             next_big = max(nums[i + 1:])
    #             return next_big
    #     count = 0
    #     for i in range(len(height)):
    #         if i != 0 and i != len(height) - 1:
    #             left = find_next_big(height, i, left=True)
    #             right = find_next_big(height, i)
    #             if height[i] > left or height[i] > right:
    #                 continue
    #             val = min(left, right) - height[i]
    #             count += val
    #     return count

    # def trap(self, height: List[int]) -> int:
    #     # 优化第一种解法，动态规划思想
    #     # i 左边最大的为max(height[i-1],max_left[i-1])
    #     # 时间复杂度 O(n) 空间复杂度O(2*n)

    #     max_left = [0]
    #     max_right = [0]

    #     for i in range(1, len(height)):
    #         left = max(max_left[i - 1], height[i - 1])
    #         max_left.append(left)
    #         j = -i-1
    #         right = max(max_right[j + 1], height[j + 1])
    #         max_right.insert(0, right)
    #     count = 0
    #     for i in range(len(height)):
    #         min_height = min(max_left[i], max_right[i])
    #         if height[i] >= min_height:
    #             continue
    #         count += min_height - height[i]
    #     return count

    def trap(self, height: List[int]) -> int:
        # 单调栈
        # 时间复杂度 O(n) 空间复杂度O(2*n)

        stack = []
        current = 0
        count = 0

        while current < len(height):

            # 如果当前高度大于栈顶高度
            while stack and height[current] > height[stack[-1]]:
                # 要出栈的元素
                h = stack.pop()
                if not stack:
                    break
                # 两堵墙间的距离
                distance = current - stack[-1] - 1
                min_height = min(height[stack[-1]], height[current])
                count += distance*(min_height-height[h])

            stack.append(current)
            current += 1
        return count
        # @lc code=end
