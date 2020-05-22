#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     def helper(pre_l, pre_r, in_l, in_r):
    #         if pre_l > pre_r:
    #             return None

    #         # 前序遍历第一个节点是根节点
    #         preorder_root = pre_l
    #         # 找到中序遍历根节点位置
    #         inorder_root = table[preorder[pre_l]]

    #         # 先找出根节点
    #         root = TreeNode(preorder[preorder_root])

    #         # 得到左子树中的节点数目
    #         left_subtree_size = inorder_root-in_l

    #         # 递归的构造左子树
    #         root.left = helper(pre_l + 1, pre_l +
    #                            left_subtree_size, in_l, inorder_root - 1)
    #         root.right = helper(pre_l + left_subtree_size + 1,
    #                             pre_r, inorder_root + 1, in_r)
    #         return root

    #     table = {elem: i for i, elem in enumerate(inorder)}
    #     n = len(preorder)
    #     return helper(0, n - 1, 0, n - 1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        # 找出根节点在中序遍历里的位置
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root


# @lc code=end
