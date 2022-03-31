#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def invertTree(self, root: TreeNode) -> TreeNode:
    #     # recursive solution
    #     # time complexity: O(n)
    #     # space compexity: O(n)

    #     if not root:
    #         return root

    #     leftNode = self.invertTree(root.left)
    #     rightNode = self.invertTree(root.right)

    #     root.left = rightNode
    #     root.right = leftNode

    #     return root

    def invertTree(self, root: TreeNode) -> TreeNode:
        # iterative solution with stack
        # time complexity: O(n)
        # space compexity: O(n)

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.left)
                stack.append(node.right)
        return root

# @lc code=end
