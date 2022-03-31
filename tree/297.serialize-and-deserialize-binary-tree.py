# @before-stub-for-debug-begin
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    '''
    1.DFS solutions, preorder traverse
    '''

    # def serialize(self, root):
    #     """Encodes a tree to a single string.

    #     :type root: TreeNode
    #     :rtype: str
    #     """
    #     if not root:
    #         return "x"

    #     left = self.serialize(root.left)
    #     right = self.serialize(root.right)
    #     return "{},{},{}".format(str(root.val), left, right)

    # def deserialize(self, data):
    #     """Decodes your encoded data to tree.

    #     :type data: str
    #     :rtype: TreeNode
    #     """

    #     from collections import deque
    #     nodeList = data.split(",")

    #     q = deque(nodeList)

    #     def buildTree():
    #         val = q.popleft()
    #         if val == "x":
    #             return None

    #         node = TreeNode(val)
    #         node.left = buildTree()
    #         node.right = buildTree()
    #         return node

    #     return buildTree()

    '''
    2.DFS solutions, postorder traverse
    '''

    # def serialize(self, root):
    #     if not root:
    #         return "x"

    #     left = self.serialize(root.left)
    #     right = self.serialize(root.right)
    #     return "{},{},{}".format(left, right, str(root.val))

    # def deserialize(self, data):
    #     from collections import deque
    #     nodeList = data.split(",")

    #     q = deque(nodeList)

    #     def buildTree():
    #         val = q.pop()
    #         if val == "x":
    #             return None

    #         node = TreeNode(val)
    #         node.right = buildTree()
    #         node.left = buildTree()
    #         return node

    #     return buildTree()

    '''
    3.BFS solutions, level order traverse
    '''

    def serialize(self, root):
        from collections import deque

        s = ""
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node:
                s += "{},".format(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                s += "x,"
        return s[:-1]

    # def deserialize(self, data):
    #     # first way for iterating
    #     from collections import deque

    #     nodeList = data.split(',')
    #     if nodeList[0] == "x":
    #         return None

    #     q = deque()
    #     root = TreeNode(nodeList[0])
    #     q.append(root)

    #     i = 1
    #     while i < len(nodeList):

    #         node = q.popleft()

    #         # left child
    #         val = nodeList[i]
    #         i += 1
    #         if val != "x":
    #             node.left = TreeNode(val)
    #             q.append(node.left)

    #         # right child
    #         val = nodeList[i]
    #         i += 1
    #         if val != "x":
    #             node.right = TreeNode(val)
    #             q.append(node.right)

    #     return root

    def deserialize(self, data):
        # second way for iterating : using deque
        from collections import deque

        nodeList = deque(data.split(','))
        if nodeList[0] == "x":
            return None

        q = deque()
        root = TreeNode(nodeList.popleft())
        q.append(root)

        while nodeList:

            node = q.popleft()

            # left child
            val = nodeList.popleft()
            if val != "x":
                node.left = TreeNode(val)
                q.append(node.left)

            # right child
            val = nodeList.popleft()
            if val != "x":
                node.right = TreeNode(val)
                q.append(node.right)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end
