#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     # recursive solution
    #     # time complexity: O(n)
    #     # space complexity: O(n) (call stack space)
    #     result = []

    #     def helper(node: Optional[TreeNode]):
    #         if not node:
    #             return

    #         helper(node.left)
    #         result.append(node.val)
    #         helper(node.right)

    #     helper(root)
    #     return result

    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     # mark node status: visited or not visited
    #     # using stack
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     stack = [(root, False)]
    #     result = []

    #     while stack:
    #         node, visited = stack.pop()
    #         if not node:
    #             continue
    #         if not visited:
    #             stack.append((node.right, False))
    #             stack.append((node, True))
    #             stack.append((node.left, False))
    #         else:
    #             result.append(node.val)
    #     return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # using stack
        # time complexity: O(n)
        # space complexity: O(n)
        stack = []
        result = []
        node = root

        while stack or node:

            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result


# @lc code=end
