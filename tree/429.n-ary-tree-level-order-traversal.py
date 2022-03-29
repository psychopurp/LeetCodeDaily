#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


from typing import List


class Solution:
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    #     # recursive
    #     # time complexity: O(n)
    #     # space complexity: O(n) using in call stack

    #     result = []

    #     def helper(node: 'Node', level: int):
    #         if not node:
    #             return

    #         if len(result) == level:
    #             result.append([])

    #         result[level].append(node.val)
    #         for child in node.children:
    #             helper(child, level+1)

    #     helper(root, 0)
    #     return result

    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    #     # iterative solution, using stack. stack item: (node,level)
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     if not root:
    #         return []

    #     result, stack = [], [(root, 0)]

    #     while stack:
    #         node, level = stack.pop()
    #         if len(result) == level:
    #             result.append([])

    #         result[level].append(node.val)
    #         for i in range(len(node.children)-1, -1, -1):
    #             if node.children[i]:
    #                 stack.append((node.children[i], level+1))

    #     return result

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # iterative solution, using queue. stack item: (node,level)
        # time complexity: O(n)
        # space complexity: O(n)

        from collections import deque

        if not root:
            return []

        result = []
        q = deque()
        q.append((root, 0))
        while q:
            node, level = q.popleft()
            if len(result) == level:
                result.append([])

            result[level].append(node.val)
            for child in node.children:
                if child:
                    q.append((child, level+1))
        return result


# @lc code=end
