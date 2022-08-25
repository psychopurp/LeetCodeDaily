#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] Minesweeper
#

# @lc code=start
from typing import List, Tuple


class Solution:
    # def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    #     # DFS
    #     # time complexity: O(M*N) M*N= whole board
    #     # space complexity: O(M*N)
    #     def backtracking(candidates: List[int], step: List[int]):
    #         if len(step) == 2:
    #             permutations.append((step[0], step[1]))
    #             return
    #         for i in candidates:
    #             step.append(i)
    #             backtracking(candidates, step)
    #             step.pop()

    #     permutations: List[Tuple[int, int]] = []
    #     backtracking([0, 1, -1], [])

    #     def get_borders(pos: Tuple[int, int]) -> List[Tuple[int, int]]:
    #         ret = []
    #         x, y = pos

    #         for step in permutations:
    #             np = (x+step[0], y+step[1])
    #             if np == pos:
    #                 continue

    #             if np[0] < 0 or np[0] >= len(board) or np[1] < 0 or np[1] >= len(board[0]):
    #                 continue

    #             ret.append(np)
    #         return ret

    #     def dfs(pos: Tuple[int, int]):
    #         x, y = pos

    #         if board[x][y] == "M":
    #             board[x][y] = "X"
    #             return

    #         nps = get_borders(pos)
    #         m = 0
    #         for np in nps:
    #             if board[np[0]][np[1]] == "M":
    #                 m += 1
    #         if m > 0:
    #             board[x][y] = str(m)
    #         else:
    #             board[x][y] = "B"
    #             for np in nps:
    #                 if board[np[0]][np[1]] == "E":
    #                     dfs(np)

    #     dfs((click[0], click[1]))
    #     return board

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # BFS
        # time complexity: O(M*N) M*N= whole board
        # space complexity: O(M*N)

        from collections import deque

        directions: List[Tuple[int, int]] = [
            (-1, -1), (-1, 1), (-1, 0), (1, -1), (1, 1), (1, 0), (0, -1), (0, 1)]

        q = deque([(click[0], click[1])])

        while q:

            n = len(q)
            for _ in range(len(q)):
                x, y = q.popleft()
                if board[x][y] == "M":
                    board[x][y] = "X"
                    return board
                if board[x][y] == "E":
                    mines = 0
                    nps: List[Tuple[int, int]] = []
                    for d in directions:
                        np = (x+d[0], y+d[1])
                        if np[0] < 0 or np[0] >= len(board) or np[1] < 0 or np[1] >= len(board[0]):
                            continue

                        if board[np[0]][np[1]] == "M":
                            mines += 1

                        if board[np[0]][np[1]] == "E":
                            nps.append(np)
                    if mines > 0:
                        board[x][y] = str(mines)
                    else:
                        board[x][y] = "B"
                        for np in nps:
                            q.append(np)

        return board
# @lc code=end
