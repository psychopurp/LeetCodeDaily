#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     # recursive solution with DFS : check boundary of every nodes
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     def check(node: TreeNode, leftBound, rightBound) -> bool:
    #         if not node:
    #             return True

    #         if node.val <= leftBound or node.val >= rightBound:
    #             return False

    #         right = check(node.right, node.val, rightBound)
    #         left = check(node.left, leftBound, node.val)

    #         return right and left

    #     return check(root, float('-inf'), float('inf'))

    # def isValidBST(self, root: TreeNode) -> bool:
    #     # iterative solution with DFS : inorder traversal
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     stack = [(root, False)]
    #     pre = float('-inf')

    #     while stack:

    #         node, visited = stack.pop()
    #         if not node:
    #             continue

    #         if not visited:
    #             stack.append((node.right, False))
    #             stack.append((node, True))
    #             stack.append((node.left, False))
    #         else:
    #             if node.val <= pre:
    #                 return False
    #             pre = node.val

    #     return True

    # def isValidBST(self, root: TreeNode) -> bool:
    #     # recursive solution with DFS : inorder traversal
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     pre = float('-inf')

    #     def dfs(node: TreeNode) -> bool:
    #         nonlocal pre
    #         if not node:
    #             return True

    #         if not dfs(node.left):
    #             return False

    #         if node.val <= pre:
    #             return False

    #         pre = node.val

    #         return dfs(node.right)

    #     return dfs(root)

    def isValidBST(self, root: TreeNode) -> bool:
        # iterative solution with DFS : inorder traversal
        # time complexity: O(n)
        # space complexity: O(n)

        stack = []
        pre = float('-inf')

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val <= pre:
                    return False
                pre = root.val
                root = root.right

        return True

# @lc code=end
