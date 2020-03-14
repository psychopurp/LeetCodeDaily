#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column=[[0]*9 for i in range(9)]
        box=[[0]*9 for i in range(9)]
        for i in range(9):
            row=[0]*9
            for j in range(9):
                if board[i][j]=='.':
                    continue
                else:
                    tmp= int(board[i][j])-1
                    box_index = (i // 3 ) * 3 + j // 3
                    row[tmp]+=1
                    column[j][tmp]+=1
                    box[box_index][tmp]+=1
                    if row[tmp]>1 or column[j][tmp]>1 or box[box_index][tmp]>1:
                        return False
        return True

# @lc code=end


'''
[["5","3",".",".","7",".",".",".","."]
 ["6",".",".","1","9","5",".",".","."]
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]
'''