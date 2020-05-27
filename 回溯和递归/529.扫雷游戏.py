#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        row = len(board)
        col = len(board[0])

        def DFS(x, y):
            if board[x][y] == 'E':
                m_count = 0
                for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]:
                    if 0 <= r < row and 0 <= c < col:
                        if board[r][c] == 'M':
                            m_count += 1
                board[x][y] = str(m_count) if m_count != 0 else 'B'
                # 如果是有炸弹那就不递归
                if m_count != 0:
                    return
                for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]:
                    if 0 <= r < row and 0 <= c < col:
                        DFS(r, c)

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = "X"
            return board
        DFS(*click)
        return board


# @lc code=end
