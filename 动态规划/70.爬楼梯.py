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

    # def climbStairs(self, n: int) -> int:
    #     if n <= 2:
    #         return n
    #     first, second = 1, 2
    #     cur = first + second
    #     for i in range(3, n):
    #         first, second = second, cur
    #         cur = first+second

    #     return cur

    def climbStairs(self, n: int) -> int:
        # 递归加备忘录 时间复杂度O(N) 空间复杂度O(N)
        def helper(memo, n):
            if n <= 2:
                return n
            if memo[n - 1] != 0:
                return memo[n-1]
            memo[n-1] = helper(memo, n - 1) + helper(memo, n - 2)
            return memo[n-1]

        dp_table = [0]*n
        return helper(dp_table, n)

# @lc code=end
