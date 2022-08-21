#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # DFS: iterative
        # time complexity: O(N)
        # space complexity: O(N)

        if not root:
            return []

        stack = []
        stack.append((root, 0))
        result = []

        while stack:
            node, level = stack.pop()
            if len(result) == level:
                result.append(node.val)
            else:
                result[level] = max(result[level], node.val)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))

        return result
# @lc code=end
