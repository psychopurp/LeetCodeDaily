#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS : get max gain of each node, max gain of node = max(node.val,node.val+left,node.val+right,node.val+left+right)
        # time complexity: O(n)
        # space complexity: O(n)

        self.maxSum = float('-inf')

        def maxGain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)

            self.maxSum = max(self.maxSum, leftGain + rightGain + node.val)

            return node.val+max(leftGain, rightGain)

        maxGain(root)
        return self.maxSum

# @lc code=end
