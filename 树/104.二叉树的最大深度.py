#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    #     # 递归实现
    #     if not root:
    #         return 0
    #     left_hegiht = self.maxDepth(root.left)
    #     right_hegight = self.maxDepth(root.right)
    #     return max(left_hegiht, right_hegight)+1

    # def maxDepth(self, root: TreeNode) -> int:
    #     # DFS实现
    #     stack = []
    #     if root:
    #         stack.append((1, root))
    #     depth = 0
    #     while len(stack) != 0:
    #         current_depth, node = stack.pop()
    #         if node:
    #             depth = max(current_depth, depth)
    #             stack.append((current_depth + 1, node.left))
    #             stack.append((current_depth + 1, node.right))
    #     return depth

    def maxDepth(self, root: TreeNode) -> int:
        # BFS实现
        stack = []
        if root:
            stack.append((1, root))
        depth = 0
        while len(stack) != 0:
            current_depth, node = stack.pop(0)
            if node:
                depth = max(current_depth, depth)
                stack.append((current_depth + 1, node.left))
                stack.append((current_depth + 1, node.right))
        return depth


# @lc code=end
