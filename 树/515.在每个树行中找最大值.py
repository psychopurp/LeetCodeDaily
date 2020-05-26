#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            child = None
            node = []
            for i in queue:
                if child == None:
                    child = i.val
                elif i.val > child:
                    child = i.val
                if i.left:
                    node.append(i.left)
                if i.right:
                    node.append(i.right)
            res.append(child)
            queue = node
        return res


# @lc code=end
