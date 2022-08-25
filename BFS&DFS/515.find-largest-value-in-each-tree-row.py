#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def largestValues(self, root: Optional[TreeNode]) -> List[int]:
    #     # DFS: iterative
    #     # time complexity: O(N)
    #     # space complexity: O(N)

    #     if not root:
    #         return []

    #     stack = []
    #     stack.append((root, 0))
    #     result = []

    #     while stack:
    #         node, level = stack.pop()
    #         if len(result) == level:
    #             result.append(node.val)
    #         else:
    #             result[level] = max(result[level], node.val)
    #         if node.left:
    #             stack.append((node.left, level+1))
    #         if node.right:
    #             stack.append((node.right, level+1))

    #     return result

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # BFS: level order traversal
        # time complexity: O(N)
        # space complexity: O(N)

        from collections import deque
        if not root:
            return []

        q = deque([root])
        ans = []
        level = 0
        while q:
            if len(ans) == level:
                ans.append(q[0].val)

            n = len(q)
            for _ in range(n):
                node = q.popleft()
                ans[level] = max(ans[level], node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            level += 1

        return ans

# @lc code=end
