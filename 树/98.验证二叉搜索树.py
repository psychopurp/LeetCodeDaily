#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    #     #自己的解法 递归中序遍历
    #     stack = []

    #     def recursive(root):
    #         if root is None:
    #             return
    #         recursive(root.left)
    #         stack.append(root.val)
    #         recursive(root.right)
    #     recursive(root)

    #     for i in range(len(stack)-1):
    #         if stack[i] >= stack[i+1]:
    #             return False
    #     return True

    # def isValidBST(self, root: TreeNode) -> bool:
    #     # 递归解法
    #     def helper(root, lower=float('-inf'), upper=float('inf')):
    #         ''' 递归，左边界和右边界'''
    #         if not root:
    #             return True
    #         val = root.val
    #         if val <= lower or val >= upper:
    #             return False
    #         if helper(root.left, lower, val) is False:
    #             return False
    #         if helper(root.right, val, upper) is False:
    #             return False
    #         return True
    #     return helper(root)

    # def isValidBST(self, root: TreeNode) -> bool:
    #     # 递归解法通过栈转换成迭代解法
    #     stack = []
    #     if not root:
    #         return True
    #     stack.append((root, float('-inf'), float('inf')))
    #     while len(stack) != 0:
    #         root, lower, upper = stack.pop()
    #         if root.val <= lower or root.val >= upper:
    #             return False
    #         if root.left:
    #             stack.append((root.left, lower, root.val))
    #         if root.right:
    #             stack.append((root.right, root.val, upper))
    #     return True

    def isValidBST(self, root: TreeNode) -> bool:
        # 非递归中序遍历的方法
        stack = []
        if not root:
            return True
        boundary = float('-inf')
        while True:

            if root:
                stack.append(root)
                root = root.left
                continue
            elif len(stack) != 0:
                root = stack.pop()
                if root.val <= boundary:
                    return False
                boundary = root.val
                root = root.right
                continue
            else:
                break
        return True


# @lc code=end
