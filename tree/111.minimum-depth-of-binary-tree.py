#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def minDepth(self, root: TreeNode) -> int:
    #     # DFS with stack
    #     # time complexity: O(n)
    #     # space compexity: O(n)

    #     if not root:
    #         return 0

    #     stack = [(root, 1)]
    #     ans = float("inf")

    #     while stack:
    #         node, level = stack.pop()
    #         if not node.left and not node.right:
    #             ans = min(ans, level)
    #         if node.left:
    #             stack.append((node.left, level+1))
    #         if node.right:
    #             stack.append((node.right, level+1))

    #     return ans

    def minDepth(self, root: TreeNode) -> int:
        # BFS with queue : level order traversal
        # time complexity: O(n)
        # space compexity: O(n)

        from collections import deque

        if not root:
            return 0

        q = deque()
        q.append((root, 1))

        while q:
            node, level = q.popleft()
            if not node:
                continue

            if not node.left and not node.right:
                return level
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))


# @lc code=end
