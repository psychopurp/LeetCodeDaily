#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # DFS
        # time complexity: O(n^2)
        # space complexity: O(n)

        if not preorder:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        head = preorder[0]
        headIndex = inorder.index(head)

        leftNodesInorder = inorder[:headIndex]
        rightNodesInorder = inorder[headIndex+1:]

        leftNodesPreorder = preorder[1:1+len(leftNodesInorder)]
        rightNodesPreorder = preorder[1+len(leftNodesInorder):]

        node = TreeNode(head)
        node.left = self.buildTree(leftNodesPreorder, leftNodesInorder)
        node.right = self.buildTree(rightNodesPreorder, rightNodesInorder)

        return node


# @lc code=end
