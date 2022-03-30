#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     # recursive solutions using DFS
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     if not p and not q:
    #         return True

    #     if not q or not p:
    #         return False

    #     if p.val != q.val:
    #         return False

    #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # DFS with stack
        # time complexity: O(n)
        # space complexity: O(n)

        stack = [(p, q)]

        while stack:
            p, q = stack.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        return True

# @lc code=end
