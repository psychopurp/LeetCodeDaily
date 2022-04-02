#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
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
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # iterative solution with DFS : inorder traversal
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     stack = []

    #     while stack or root:
    #         if root:
    #             stack.append(root)
    #             root = root.left
    #         else:
    #             root = stack.pop()
    #             k -= 1
    #             if k == 0:
    #                 return root.val

    #             root = root.right

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # iterative solution with DFS : inorder traversal
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     stack = [(root, False)]
    #     while stack:
    #         node, visited = stack.pop()
    #         if not node:
    #             continue

    #         if not visited:
    #             stack.append((node.right, False))
    #             stack.append((node, True))
    #             stack.append((node.left, False))
    #         else:
    #             k -= 1
    #             if k == 0:
    #                 return node.val

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     # recursive solution with DFS : inorder traversal
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     ans = 0

    #     def dfs(node: TreeNode):
    #         nonlocal k
    #         nonlocal ans

    #         if node.left:
    #             dfs(node.left)

    #         k -= 1
    #         if k == 0:
    #             ans = node.val
    #             return

    #         if node.right:
    #             dfs(node.right)

    #     dfs(root)
    #     return ans

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # recursive solution with binary search
        # time complexity: O(n)
        # space complexity: O(n)

        def countNodes(node: TreeNode) -> int:
            if not node:
                return 0

            return countNodes(node.left)+countNodes(node.right)+1

        count = countNodes(root.left)
        if k <= count:
            return self.kthSmallest(root.left, k)

        if k > count+1:
            return self.kthSmallest(root.right, k-count-1)

        return root.val


# @lc code=end
