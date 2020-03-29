#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # 递归

        def helper(left, right):
            if left >= right:
                return None
            mid = (left+right) // 2
            head = TreeNode(nums[mid])
            left_head = helper(left, mid)
            right_head = helper(mid+1, right)
            head.left = left_head
            head.right = right_head
            return head

        return helper(0, len(nums))


# @lc code=end
