#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     # 颜色标记法 O(N) True代表未访问
    #     if not root:
    #         return []
    #     stack = [(root, True)]
    #     res = []
    #     while stack:
    #         node, isAdd = stack.pop()
    #         if not node:
    #             continue
    #         if isAdd:
    #             stack.append((node.right, True))
    #             stack.append((node, False))
    #             stack.append((node.left, True))
    #         else:
    #             res.append(node.val)
    #     return res

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #
        if not root:
            return []
        stack = []
        res = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                res.append(node.val)
                node = node.right
            else:
                break
        return res


# @lc code=end
