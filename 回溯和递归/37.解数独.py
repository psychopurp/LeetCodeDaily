#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.

    #     回溯算法
    #     """
    #     n = 9

    #     def DFS(pos: int):
    #         nonlocal valid
    #         if pos == len(spaces):
    #             valid = True
    #             return
    #         i, j = spaces[pos]
    #         for digit in range(n):
    #             if isValid(i, j, digit):
    #                 rowUsed[i][digit] = columnUsed[j][digit] = blockUsed[i //
    #                                                                      3][j//3][digit] = True
    #                 board[i][j] = str(digit+1)
    #                 DFS(pos+1)
    #                 rowUsed[i][digit] = columnUsed[j][digit] = blockUsed[i //
    #                                                                      3][j//3][digit] = False
    #             if valid:
    #                 return

    #     def isValid(i: int, j: int, digit: int) -> bool:
    #         return not (rowUsed[i][digit] or columnUsed[j][digit] or blockUsed[i//3][j//3][digit])

    #     rowUsed = [[False]*n for _ in range(n)]
    #     columnUsed = [[False]*n for _ in range(n)]
    #     blockUsed = [[[False]*n for _ in range(3)] for _a in range(3)]
    #     spaces = []
    #     valid = False

    #     for i in range(n):
    #         for j in range(n):
    #             if board[i][j] != ".":
    #                 digit = int(board[i][j])-1
    #                 rowUsed[i][digit] = True
    #                 columnUsed[j][digit] = True
    #                 blockUsed[i//3][j//3][digit] = True
    #             else:
    #                 spaces.append((i, j))

    #     DFS(0)

    def solveSudoku(self, board: List[List[str]]) -> None:
        # 回溯 使用位运算的方式优化
        n = 9

        def flip(i: int, j: int, digit: int):
            rowUsed[i] ^= (1 << digit)
            columnUsed[j] ^= (1 << digit)
            blockUsed[i//3][j//3] ^= (1 << digit)

        def dfs(pos: int):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            mask = ~(rowUsed[i] | columnUsed[j] |
                     blockUsed[i//3][j//3]) & 0x1ff

            digit = 0
            while mask:
                if mask & 1:
                    flip(i, j, digit)
                    board[i][j] = str(digit+1)
                    dfs(pos+1)
                    flip(i, j, digit)
                if valid:
                    return
                mask = mask >> 1
                digit += 1

        rowUsed = [0]*9
        columnUsed = [0]*9
        blockUsed = [[0 for _ in range(3)] for _ in range(3)]
        spaces = []
        valid = False
        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    spaces.append((i, j))
                else:
                    digit = int(board[i][j])-1
                    flip(i, j, digit)

        dfs(0)


# @lc code=end
