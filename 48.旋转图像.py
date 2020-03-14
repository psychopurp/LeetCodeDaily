#
# @lc app=leetcode.cn id=48 lang=python3
#
# [48] 旋转图像
#

# @lc code=start


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            # print('第{}'.format(i))
            m = n - 2 * i - 1
            # print('宽度 {}'.format(n - 2 * i - 1))
            index = 0
            for j in range(i, n-i-1):
                tmp = matrix[i][j]
                # # matrix[i][j] = matrix[][j]
                # matrix[m-j][i] = matrix[i+m][m-j]
                matrix[i][j+m-2*index-m+2*index] = matrix[j+m-2*index][i]
                matrix[j+m-2*index][i] = matrix[i+m][j+m-2*index]
                matrix[i+m][j+m-2*index] = matrix[j][i+m]
                matrix[j][i + m] = tmp
                index += 1
# @lc code=end


# '''
# [15,4, 2, 5,1],
# [15,4, 2, 5,1],
# [15,4, 2, 5,1],
# [15,4, 2, 5,1],
# [15,4, 2, 5,1],
# '''


# def rotate(matrix):
#     n = len(matrix)
#     for i in range(n//2):
#         # print('第{}'.format(i))
#         m = n - 2 * i - 1
#         # print('宽度 {}'.format(n - 2 * i - 1))
#         index = 0
#         for j in range(i, n-i-1):
#             tmp = matrix[i][j]
#             # # matrix[i][j] = matrix[][j]
#             # matrix[m-j][i] = matrix[i+m][m-j]
#             matrix[i][j+m-2*index-m+2*index] = matrix[j+m-2*index][i]
#             matrix[j+m-2*index][i] = matrix[i+m][j+m-2*index]
#             matrix[i+m][j+m-2*index] = matrix[j][i+m]
#             matrix[j][i + m] = tmp
#             index += 1

            # print(j)

        # tmp_length=n-2*i
        # for j in range(tmp_length-1):
        #     m=tmp_length-1+i
        #     tmp=matrix[i][j+i]
        #     matrix[i][j+i]=matrix[m-j-i][i]
        #     matrix[m-j-i][i]=matrix[m][m-j]
        #     matrix[m][m-j-i]=matrix[j+i][m]
        #     matrix[j+i][m]=tmp
# matrix = [
#     [5, 1, 9, 11],
#     [2, 4, 8, 10],
#     [13, 3, 6, 7],
#     [15, 14, 12, 16]
# ]

# rotate(matrix)
