#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 时间复杂度O(N!) 空间复杂度O(N)

        def dfs(row, track):
            if row == n:
                res.append(track[:])
                return

            for col in range(n):
                if col in column or col+row in pie or row-col in na:
                    continue

                track.append(col)
                column.add(col)
                na.add(row - col)
                pie.add(row + col)
                dfs(row + 1, track)
                track.pop()
                column.remove(col)
                na.remove(row - col)
                pie.remove(row + col)

        res = []
        column = set()
        pie = set()
        na = set()
        dfs(0, [])
        # return res
        return [['.'*i+'Q'+'.'*(n-i-1) for i in case] for case in res]


# @lc code=end
