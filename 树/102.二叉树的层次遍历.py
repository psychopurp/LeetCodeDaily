#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     # 通过前序遍历递归实现
    #     result = []

    #     def helper(root, level):
    #         if not root:
    #             return
    #         if level == len(result):
    #             result.append([])
    #         result[level].append(root.val)
    #         helper(root.left, level + 1)
    #         helper(root.right, level + 1)

    #     helper(root, 0)
    #     return result

    # def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #     # 迭代实现
    #     result = []
    #     level = 0
    #     queue = [(root, level)]

    #     while queue:
    #         node, level = queue.pop(0)
    #         if not node:
    #             continue
    #         if len(result) == level:
    #             result.append([])
    #         result[level].append(node.val)
    #         queue.append((node.left, level+1))
    #         queue.append((node.right, level + 1))
    #     return result

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # 广度优先搜索
        from collections import deque
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)

        while queue:
            child = deque()
            cur = []
            for node in queue:
                if not node:
                    continue
                cur.append(node.val)
                if node.left:
                    child.append(node.left)
                if node.right:
                    child.append(node.right)
            result.append(cur)
            queue = child

        return result

        # @lc code=end
