#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List, Set, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # DFS backtracking solution
        # time complexity: O(N*N)
        # space complexity: O(N*N)
        n = len(board)

        def dfs(visit_idx: int) -> bool:
            if visit_idx == len(spaces):
                return True

            i, j = spaces[visit_idx]

            for v in range(1, n + 1):
                val = str(v)
                if (
                    val not in row[i]
                    and val not in col[j]
                    and val not in block[i // 3 * 3 + j // 3]
                ):
                    row[i].add(val)
                    col[j].add(val)
                    block[i // 3 * 3 + j // 3].add(val)

                    board[i][j] = val
                    if dfs(visit_idx + 1):
                        return True
                    board[i][j] = "."

                    row[i].remove(val)
                    col[j].remove(val)
                    block[i // 3 * 3 + j // 3].remove(val)

            return False

        spaces = []
        row: List[Set[str]] = [set() for _ in range(n)]
        col: List[Set[str]] = [set() for _ in range(n)]
        block: List[Set[str]] = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    val = board[i][j]
                    row[i].add(val)
                    col[j].add(val)
                    block[i // 3 * 3 + j // 3].add(val)

        dfs(0)


# @lc code=end
