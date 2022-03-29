# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N-ary Tree Preorder Traversal
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
    # def preorder(self, root: 'Node') -> List[int]:
    #     # recursive
    #     # time complexity: O(n)
    #     # space complexity: O(n) using in call stack

    #     result = []

    #     def helper(node: 'Node'):
    #         if not node:
    #             return

    #         result.append(node.val)
    #         for child in node.children:
    #             helper(child)

    #     helper(root)
    #     return result

    # def preorder(self, root: 'Node') -> List[int]:
    #     # iterative solution, using stack
    #     # time complexity: O(n)
    #     # space complexity: O(n)
    #     if not root:
    #         return []

    #     result = []
    #     stack = [root]

    #     while stack:
    #         node = stack.pop()
    #         result.append(node.val)
    #         for i in range(len(node.children)-1, -1, -1):
    #             if node.children[i]:
    #                 stack.append(node.children[i])
    #     return result

    def preorder(self, root: 'Node') -> List[int]:
        # mark node status: visited or not visited
        # time complexity: O(n)
        # space complexity: O(n)

        if not root:
            return []

        result, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if not visited:
                for i in range(len(node.children)-1, -1, -1):
                    if node.children[i]:
                        stack.append((node.children[i], False))
                stack.append((node, True))
            else:
                result.append(node.val)

        return result

    # @lc code=end
