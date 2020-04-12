#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [(root, 0)]
        levels = []
        while queue:
            node, level = queue.pop(0)
            if level == len(levels):
                levels.append([])
            if level % 2 == 0:
                levels[level].append(node.val)
            else:
                levels[level].insert(0, node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return levels
        # @lc code=end
