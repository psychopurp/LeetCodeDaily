#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] Binary Tree Paths
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # solution 1: backtracking
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        result=[]
        def backtrack(node,path):
            if not node.left and not node.right:
                result.append(path)
                return

            if node.left:
                backtrack(node.left,f"{path}->{node.left.val}")
            if node.right:
                backtrack(node.right,f"{path}->{node.right.val}")
            
                
        
        backtrack(root,str(root.val))
        return result
        
# @lc code=end

