#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    #     if not inorder or not postorder:
    #         return None
    #     # 后序遍历最后一位是根节点
    #     root = TreeNode(postorder[-1])
    #     idx = inorder.index(postorder[-1])
    #     root.left = self.buildTree(inorder[:idx], postorder[:idx])
    #     root.right = self.buildTree(inorder[idx+1:], postorder[idx:-1])
    #     return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(in_l, in_r, pos_l, pos_r):
            if in_l > in_r:
                return None

            postorder_root = pos_r
            inorder_root = table[postorder[postorder_root]]
            left_child_size = inorder_root - in_l

            root = TreeNode(postorder[postorder_root])
            root.left = helper(in_l, inorder_root-1, pos_l,
                               pos_l+left_child_size-1)
            root.right = helper(inorder_root+1, in_r, pos_l +
                                left_child_size, postorder_root-1)
            return root

        table = {elem: i for i, elem in enumerate(inorder)}
        n = len(inorder)
        return helper(0, n-1, 0, n-1)


# @lc code=end
