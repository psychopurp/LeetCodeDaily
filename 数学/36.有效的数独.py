#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowUsed = [0]*9
        columnUsed = [0]*9
        blockUsed = [0]*9

        def flip(i, j, digit):
            rowUsed[i] ^= (1 << digit)
            columnUsed[j] ^= (1 << digit)
            blockUsed[(i // 3) * 3 + j // 3] ^= (1 << digit)

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    digit = int(board[i][j])-1
                    if (rowUsed[i] | columnUsed[j] | blockUsed[(i//3)*3+j//3]) & (1 << digit):
                        return False
                    else:
                        flip(i, j, digit)
        return True


# @lc code=end
