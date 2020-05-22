#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     self.ans = None

    #     def recurse_tree(current_node):

    #         # If reached the end of a branch, return False.
    #         if not current_node:
    #             return False

    #         left = recurse_tree(current_node.left)
    #         right = recurse_tree(current_node.right)

    #         tmp = current_node == q or current_node == p

    #         if left + right+tmp >= 2:
    #             self.ans = current_node
    #         return left or right or tmp

    #     recurse_tree(root)
    #     return self.ans

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 后序遍历DFS O(N) O(N)
        if not root or (root == q or root == p):
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


# @lc code=end
