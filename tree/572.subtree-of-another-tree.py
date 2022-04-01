#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
    #     # recursive solution with DFS
    #     # time complexity: O(root*subRoot)
    #     # space complexity: O(max(root,subRoot)) maximum call stack space

    #     if not root and not subRoot:
    #         return True

    #     if not root or not subRoot:
    #         return False

    #     return self.isSameTree(root, subRoot) or self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)

    # def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
    #     if not p and not q:
    #         return True

    #     if not p or not q:
    #         return False
    #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # serialize in preorder or inorder then compare strings
        # time complexity: O(n*m) : used in comparing strings
        # space complexity: O(max(root,subRoot)) maximum call stack space

        def convert(node: TreeNode) -> str:
            if not node:
                return "$"

            return "^"+str(node.val)+convert(node.left)+convert(node.right)

        return convert(subRoot) in convert(root)

# @lc code=end
