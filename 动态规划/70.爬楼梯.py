#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start


class Solution:
    # def climbStairs(self, n: int) -> int:
    #     # d[n]=d[n-1]+d[n-2]
    #     if n <= 2:
    #         return n
    #     first = 1
    #     second = 2
    #     d = 0
    #     for i in range(3, n + 1):
    #         d = first + second
    #         first, second = second, d
    #     return d

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first, second = 1, 2
        cur = first + second
        for i in range(3, n):
            first, second = second, cur
            cur = first+second

        return cur


# @lc code=end
