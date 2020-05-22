#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        res = []
        while queue:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append("null")
        while res and res[-1] == 'null':
            res.pop()
        return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # data = data.replace("null", "None")
        data = eval(data)
        nodes = [TreeNode(v) if v != None else None for v in data]

        for i in range(1, len(nodes)):
            node = nodes[i]
            parent = nodes[(i - 1) // 2]
            if i % 2 == 0:
                parent.right = node
            else:
                parent.left = node
        return nodes[0] if nodes else None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
