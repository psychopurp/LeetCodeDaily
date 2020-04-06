#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#

# @lc code=start


class Solution:
    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     # DFS

    #     n = len(M)
    #     visited = set()
    #     count = 0

    #     def dfs(i):
    #         # 访问第i个人
    #         for j in range(n):
    #             if j not in visited and M[i][j] == 1:
    #                 visited.add(j)
    #                 dfs(j)
    #     for i in range(n):
    #         if i not in visited:
    #             visited.add(i)
    #             dfs(i)
    #             count += 1
    #     return count

    # def findCircleNum(self, M: List[List[int]]) -> int:
    #     # BFS
    #     n = len(M)
    #     visited = set()
    #     count = 0
    #     for i in range(n):
    #         tmp = []
    #         if i not in visited:
    #             tmp.append(i)
    #             count += 1
    #         while tmp:
    #             cur = tmp.pop(0)
    #             if cur in visited:
    #                 continue
    #             else:
    #                 visited.add(cur)
    #             for j in range(n):
    #                 if j != cur and M[cur][j] == 1:
    #                     tmp.append(j)
    #     return count

    def findCircleNum(self, M: List[List[int]]) -> int:
        # Union-find 并查集算法
        n = len(M)
        parent = [i for i in range(n)]
        # 连通数
        self.count = n
        # 连接p，q

        def union(p, q):
            root_p = find(p)
            root_q = find(q)
            if root_p == root_q:
                return
            parent[root_p] = root_q
            # 如果连通则数量减一
            self.count -= 1

        # 返回 x 的根节点
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    union(i, j)
        return self.count
    # @lc code=end
