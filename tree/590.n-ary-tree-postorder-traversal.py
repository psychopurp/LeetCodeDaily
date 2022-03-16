# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
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
    # def postorder(self, root: 'Node') -> List[int]:
    #     # recursively
    #     # time complexity: O(n)
    #     # space complexity: O(n) using in call stack

    #     if not root:
    #         return []

    #     result = []

    #     def helper(node: 'Node'):
    #         for child in node.children:
    #             helper(child)

    #         result.append(node.val)

    #     helper(root)
    #     return result

    def postorder(self, root: 'Node') -> List[int]:
        # mark node status: visited or not visited
        # time complexity: O(n)
        # space complexity: O(n)

        if not root:
            return []

        stack = [(root, False)]
        result = []

        while stack:
            node, visited = stack.pop()
            if not visited:
                n = len(node.children)
                stack.append((node, True))
                for i in range(len(node.children)):
                    stack.append((node.children[n-i-1], False))
            else:
                result.append(node.val)

        return result

    # @lc code=end
