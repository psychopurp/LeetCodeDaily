#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 叶子节点的定义是左孩子和右孩子都为 null 时叫做叶子节点
        # 当 root 节点左右孩子都为空时，返回 1
        # 当 root 节点左右孩子有一个为空时，返回不为空的孩子节点的深度
        # 当 root 节点左右孩子都不为空时，返回左右孩子较小深度的节点值

        if not root:
            return 0

        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right))+1


# @lc code=end
