#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     # 自己第一次的解法时间复杂度O(N)
    #     def helper(node):
    #         if not node:
    #             return
    #         node.left, node.right = node.right, node.left
    #         helper(node.left)
    #         helper(node.right)
    #     helper(root)
    #     return root

    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     if root:
    #         # 左孩子等于反转后的右孩子
    #         root.left, root.right = self.invertTree(
    #             root.right), self.invertTree(root.left)
    #         return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        # 非递归解法
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root


# @lc code=end
