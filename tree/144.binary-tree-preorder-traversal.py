#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     # recursively
    #     # time complexity: O(n)
    #     # space complexity: O(n) using in call stack

    #     result = []

    #     def helper(node: Optional[TreeNode]):
    #         if not node:
    #             return

    #         result.append(node.val)
    #         helper(node.left)
    #         helper(node.right)

    #     helper(root)
    #     return result

    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     # mark node status: visited or not visited
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     stack = [(root, False)]
    #     result = []

    #     while stack:
    #         node, visited = stack.pop()
    #         if not node:
    #             continue
    #         if not visited:
    #             if node.right:
    #                 stack.append((node.right, False))
    #             if node.left:
    #                 stack.append((node.left, False))
    #             stack.append((node, True))
    #         else:
    #             result.append(node.val)

    #     return result

    # def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     # using stack to monitor call stack
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     result = []
    #     stack = []
    #     node = root

    #     while stack or node:
    #         if node:
    #             result.append(node.val)
    #             stack.append(node)
    #             node = node.left
    #         else:
    #             node = stack.pop()
    #             node = node.right
    #     return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # using stack to monitor call stack
        # time complexity: O(n)
        # space complexity: O(n)

        if not root:
            return []

        result, stack = [], [root]

        while stack:
            node = stack.pop()
            result.append(node.val)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result

# @lc code=end
