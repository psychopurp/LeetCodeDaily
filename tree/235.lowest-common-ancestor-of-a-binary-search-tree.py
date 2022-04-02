#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # DFS solution with postorder traversal
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     if not root:
    #         return None

    #     if root == p or root == q:
    #         return root

    #     left = self.lowestCommonAncestor(root.left, p, q)
    #     right = self.lowestCommonAncestor(root.right, p, q)

    #     if left and right:
    #         return root
    #     elif left:
    #         return left
    #     else:
    #         return right

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative solution : using map to record parent node
        # time complexity: O(n)
        # space complexity: O(n) using in stack and maps

        stack = [(root, 0)]
        parentMap, levelMap = {}, {}

        while stack:
            node, level = stack.pop()
            if not node:
                continue

            levelMap[node] = level

            if node.left:
                parentMap[node.left] = node
                stack.append((node.left, level+1))
            if node.right:
                parentMap[node.right] = node
                stack.append((node.right, level+1))

        # make nodes at same level
        def jumpParent(node, level):
            if level == 0:
                return node

            return jumpParent(parentMap[node], level-1)

        if levelMap[p] < levelMap[q]:
            q = jumpParent(q, levelMap[q]-levelMap[p])
        else:
            p = jumpParent(p, levelMap[p]-levelMap[q])

        while p != q:
            p = parentMap[p]
            q = parentMap[q]

        return p

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # DFS solution with postorder traversal
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     ans = None

    #     def dfs(node) -> True:
    #         nonlocal ans
    #         if ans:
    #             return True

    #         if not node:
    #             return False

    #         left = dfs(node.left)
    #         right = dfs(node.right)
    #         parent = node == p or node == q

    #         if left+right+parent >= 2 and not ans:
    #             ans = node

    #         return left or right or parent

    #     dfs(root)
    #     return ans

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # binary search : p and q must be on both sides of root
    #     # time complexity: O(n)
    #     # space complexity: O(1)

    #     while not (p.val <= root.val <= q.val or q.val <= root.val <= p.val):

    #         if p.val < root.val:
    #             root = root.left
    #         else:
    #             root = root.right
    #     return root

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     # binary search with DFS : p and q must be on both sides of root
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
    #         return root
    #     return self.lowestCommonAncestor(root.left if p.val < root.val else root.right, p, q)

# @lc code=end
