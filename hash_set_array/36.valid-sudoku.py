#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List, Set


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Hash Set
        # time complexity: O(1)
        # space complexity: O(1)
        n = len(board)

        col: List[Set[str]] = [set() for _ in range(n)]
        row: List[Set[str]] = [set() for _ in range(n)]
        block: List[Set[str]] = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] != ".":
                    val = board[i][j]
                    if (
                        val in row[i]
                        or val in col[j]
                        or val in block[i // 3 * 3 + j // 3]
                    ):
                        return False

                    col[j].add(val)
                    row[i].add(val)
                    block[i // 3 * 3 + j // 3].add(val)

        return True


# @lc code=end
