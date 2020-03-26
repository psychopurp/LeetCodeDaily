#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def isSymmetric(self, root: TreeNode) -> bool:
    #     # 层序遍历
    #     if not root:
    #         return True
    #     level = 0
    #     queue = [(root, level)]
    #     level_list = []
    #     while queue:
    #         node, level = queue.pop(0)
    #         if level == len(level_list):
    #             level_list.append([])
    #         if not node:
    #             level_list[level].append(None)
    #             continue
    #         level_list[level].append(node.val)
    #         queue.append((node.left, level+1))
    #         queue.append((node.right, level+1))
    #     for i in level_list:
    #         for j in range(len(i)//2):
    #             if i[j] != i[len(i) - 1 - j]:
    #                 return False
    #     return True

    # def isSymmetric(self, root: TreeNode) -> bool:
    #     # 递归实现
    #     if not root:
    #         return True

    #     def isMirror(left, right):
    #         if not (left or right):
    #             # 两个都为None
    #             return True
    #         if not (left and right):
    #             return False

    #         if left.val != right.val:
    #             return False
    #         return isMirror(left.left, right.right) and isMirror(left.right, right.left)
    #     return isMirror(root.left, root.right)

    def isSymmetric(self, root: TreeNode) -> bool:
        # 队列实现
        if not root:
            return True
        queue = [(root.left, root.right)]

        while queue:
            left, right = queue.pop(0)
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True


# @lc code=end
