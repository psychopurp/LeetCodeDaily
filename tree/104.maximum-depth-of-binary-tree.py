#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # recursive solution : DFS
    #     # time complexity: O(n)
    #     # space complexity: O(n) using in call stack

    #     # using list so that can change it's value in other function
    #     depthResult = [0]

    #     def helper(node: Optional[TreeNode], depth: int):
    #         if not node:
    #             return

    #         if depth > depthResult[0]:
    #             depthResult[0] = depth

    #         helper(node.left, depth+1)
    #         helper(node.right, depth+1)

    #     helper(root, 1)

    #     return depthResult[0]

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # recursive solution : max depth = max(left_max,right_max)
    #     # time complexity: O(n)
    #     # space complexity: O(n) using in call stack

    #     if not root:
    #         return 0

    #     leftDepth = self.maxDepth(root.left)
    #     rightDepth = self.maxDepth(root.right)

    #     return max(leftDepth, rightDepth)+1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # iterative solution, using stack. stack item: (node,level)
        # time complexity: O(n)
        # space complexity: O(n)

        if not root:
            return 0

        stack = [(root, 1)]
        depthResult = 0
        while stack:
            node, level = stack.pop()
            depthResult = max(depthResult, level)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))

        return depthResult

# @lc code=end
