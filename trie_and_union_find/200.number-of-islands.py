#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Union-find solution
        # time complexity: O(M*N*logMN)
        # space complexity: O(M*N)

        m, n = len(grid), len(grid[0])
        parent = [-1] * (m * n)

        def find(p: int):
            while parent[p] != p:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p: int, q: int):
            rootP = find(p)
            rootQ = find(q)
            if rootQ != rootP:
                parent[rootP] = parent[rootQ]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    key = i * n + j
                    parent[key] = key
                    if i > 0 and grid[i - 1][j] == "1":
                        union(key, (i - 1) * n + j)  # union curren+top
                    if j > 0 and grid[i][j - 1] == "1":
                        union(key, i * n + j - 1)  # union current+left

        union_set = set()

        for key in parent:
            if parent[key] != -1:
                union_set.add(find(key))

        return len(union_set)


# @lc code=end
