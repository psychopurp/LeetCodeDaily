#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        # time complexity: O(N)
        # space complexity: O(N)

        count = 0

        def dfs(node: TreeNode, max_num: int):
            nonlocal count

            if not node:
                return

            if node.val >= max_num:
                count += 1
                max_num = node.val

            dfs(node.left, max_num)
            dfs(node.right, max_num)

        dfs(root, root.val)
        return count

# @lc code=end
