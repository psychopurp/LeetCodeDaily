#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # iterating solution
        # time complexity: O(n)
        # space complexity: O(n)
        from collections import deque

        if not root:
            return []

        q = deque()
        q.append(root)

        result = []
        reverse = False

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if reverse:
                result.append(level[::-1])
                reverse = not reverse
            else:
                result.append(level)
                reverse = not reverse

        return result

# @lc code=end
