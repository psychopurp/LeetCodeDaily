#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from typing import List


class Solution:
    # def solve(self, board: List[List[str]]) -> None:
    #     # DFS
    #     # time complexity: O(M*N) Each point will only be visited once at most
    #     # space complexity: O(M*N) Stack space

    #     m, n = len(board), len(board[0])

    #     stack = []

    #     for j in range(n):
    #         if board[0][j] == "O":
    #             stack.append((0, j))
    #         if board[-1][j] == "O":
    #             stack.append((m - 1, j))

    #     for i in range(m):
    #         if board[i][0] == "O":
    #             stack.append((i, 0))
    #         if board[i][-1] == "O":
    #             stack.append((i, n - 1))

    #     while stack:
    #         x, y = stack.pop()
    #         board[x][y] = "A"

    #         for direction in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
    #             dx, dy = x + direction[0], y + direction[1]
    #             if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == "O":
    #                 stack.append((dx, dy))

    #     for i in range(m):
    #         for j in range(n):
    #             if board[i][j] == "O":
    #                 board[i][j] = "X"
    #             if board[i][j] == "A":
    #                 board[i][j] = "O"

    def solve(self, board: List[List[str]]) -> None:
        # Union-Find
        # time complexity: O(mn×α(mn)): α(n) is (Inverse Ackermann function), Specifically, it is used to describe and look up the time complexity of some algorithms such as Union-Find. In the analysis of different algorithms, α (n) is usually regarded as a very small number, which can almost be regarded as a constant.
        # space complexity: O(m*n)

        m, n = len(board), len(board[0])
        parent = [i for i in range(m * n + 1)]

        def find(x: int):
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # compression
                x = parent[x]
            return x

        def union(x: int, y: int):
            px = find(x)
            py = find(y)
            parent[px] = parent[py]

        def connected(x: int, y: int):
            px = find(x)
            py = find(y)
            return parent[px] == parent[py]

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0 or i == m - 1 or j == n - 1) and board[i][
                    j
                ] == "O":
                    # if a 'O' node is on the boundry, connect it to the dummy node
                    union(i * n + j, m * n)
                elif (
                    board[i][j] == "O"
                ):  # connect a 'O' node to its neighbour 'O' nodes
                    if board[i - 1][j] == "O":
                        union(i * n + j, (i - 1) * n + j)
                    if board[i + 1][j] == "O":
                        union(i * n + j, (i + 1) * n + j)
                    if board[i][j - 1] == "O":
                        union(i * n + j, i * n + j - 1)
                    if board[i][j + 1] == "O":
                        union(i * n + j, i * n + j + 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not connected(i * n + j, m * n):
                    board[i][j] = "X"


# @lc code=end
