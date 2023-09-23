#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Union-find solution
        # time complexity: O(N^2*logN)
        # space complexity: O(N)
        class UnionFind:
            def __init__(self, n: int) -> None:
                self.parent = [i for i in range(n)]
                self.count = n

            def find(self, parent: List[int], p: int) -> int:
                while p != parent[p]:
                    # path compression
                    parent[p] = parent[parent[p]]
                    p = parent[p]

                return p

            def union(self, p: int, q: int):
                rootP = self.find(self.parent, i)
                rootQ = self.find(self.parent, j)
                if rootP != rootQ:
                    self.parent[rootQ] = rootP
                    self.count -= 1

        n = len(isConnected)
        union_find = UnionFind(n)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    union_find.union(i, j)
        return union_find.count


# @lc code=end
