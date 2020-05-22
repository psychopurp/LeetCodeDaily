#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    # def postorder(self, root: 'Node') -> List[int]:
    #     if not root:
    #         return []

    #     stack = [(root, False)]
    #     res = []
    #     while stack:
    #         node, visited = stack.pop()
    #         if not node:
    #             continue
    #         if not visited:
    #             stack.append((node, True))
    #             for child in reversed(node.children):
    #                 stack.append((child, False))
    #         else:
    #             res.append(node.val)
    #     return res

    def postorder(self, root: 'Node') -> List[int]:

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            res.append(node.val)
            for c in node.children:
                stack.append(c)

        return res[::-1]


# @lc code=end
