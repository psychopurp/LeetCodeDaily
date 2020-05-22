#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    #     # 递归解法
    #     levels = []

    #     def helper(node, level):
    #         if not node:
    #             return
    #         if level == len(levels):
    #             levels.append([])
    #         levels[level].append(node.val)
    #         for child in node.children:
    #             helper(child, level+1)
    #     helper(root, 0)
    #     return levels

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # 非递归解法
        levels = []

        stack = [(root, 0)]

        while stack:
            node, level = stack.pop()
            if node:
                if level == len(levels):
                    levels.append([])
                levels[level].append(node.val)
                for child in node.children[::-1]:
                    stack.append((child, level + 1))
        return levels
# @lc code=end
