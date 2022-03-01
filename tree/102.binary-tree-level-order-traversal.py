#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     # iterating solution
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     from collections import deque

    #     result = []
    #     if not root:
    #         return result

    #     q = deque()
    #     q.append((root, 0))

    #     while q:
    #         node, level = q.popleft()

    #         if level == len(result):
    #             result.append([])

    #         result[level].append(node.val)
    #         if node.left:
    #             q.append((node.left, level+1))
    #         if node.right:
    #             q.append((node.right, level+1))
    #     return result

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # recursive solution
        # time complexity: O(n)
        # space complexity: O(n)
        result = []
        if not root:
            return result

        def helper(node: TreeNode, level: int):
            if len(result) == level:
                result.append([])

            result[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)

        helper(root, 0)
        return result


# @lc code=end
