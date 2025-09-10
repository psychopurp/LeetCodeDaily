#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Backtracking
        # time complexity: O(m*n*4^L) m=len(board) n=len(board[0]) L=len(word)
        # space complexity: O(m*n)

        flag = False

        def backtrack(cur_pos, index, seen: set):
            nonlocal flag
            if index == len(word):
                flag = True
                return

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = cur_pos[0]+dx, cur_pos[1]+dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == word[index] and (x, y) not in seen:
                    seen.add((x, y))
                    backtrack((x, y), index+1, seen)
                    seen.remove((x, y))

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    backtrack((i, j), 1, set([(i, j)]))

        return flag


# @lc code=end
