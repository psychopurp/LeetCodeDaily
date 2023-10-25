#
# @lc app=leetcode.cn id=552 lang=python3
#
# [552] Student Attendance Record II
#


# @lc code=start
class Solution:
    # def checkRecord(self, n: int) -> int:
    #     # 1.DFS
    #     # time complexity: O(2*3*N)
    #     # space complexity: O(2*3*N)
    #     from functools import lru_cache

    #     @lru_cache
    #     def dfs(day: int, absent: int, late: int) -> int:
    #         if day == n:
    #             return 1

    #         ans = 0

    #         # 1.put present
    #         ans = (ans + dfs(day + 1, absent, 0)) % MOD

    #         # 2.put absent
    #         if absent == 0:
    #             ans = (ans + dfs(day + 1, 1, 0)) % MOD

    #         # 3.put late
    #         if late < 2:
    #             ans = (ans + dfs(day + 1, absent, late + 1)) % MOD

    #         return ans

    #     MOD = 10**9 + 7
    #     return dfs(0, 0, 0)

    # def checkRecord(self, n: int) -> int:
    #     # 2.Bottom-up DP
    #     # time complexity: O(N)
    #     # space complexity: O(2*3*N)

    #     """
    #     dp[day][absent][late]
    #     """

    #     dp = [[[0, 0, 0] for _ in range(2)] for _ in range(n)]

    #     # initial state
    #     dp[0][0][0] = 1
    #     dp[0][0][1] = 1
    #     dp[0][1][0] = 1

    #     MOD = 10**9 + 7

    #     for i in range(1, n):
    #         dp[i][0][0] = (dp[i - 1][0][0] + dp[i - 1][0][1] + dp[i - 1][0][2]) % MOD
    #         dp[i][0][1] = dp[i - 1][0][0]
    #         dp[i][0][2] = dp[i - 1][0][1]
    #         dp[i][1][0] = (
    #             dp[i - 1][0][0]
    #             + dp[i - 1][0][1]
    #             + dp[i - 1][0][2]
    #             + dp[i - 1][1][0]
    #             + dp[i - 1][1][1]
    #             + dp[i - 1][1][2]
    #         ) % MOD

    #         dp[i][1][1] = dp[i - 1][1][0]
    #         dp[i][1][2] = dp[i - 1][1][1]

    #     summ = 0
    #     for i in range(2):
    #         for j in range(3):
    #             summ = (summ + dp[n - 1][i][j]) % MOD

    #     return summ

    # def checkRecord(self, n: int) -> int:
    #     # 3.Bottom-up DP: space optimization 1
    #     # time complexity: O(N)
    #     # space complexity: O(2*3*N)

    #     """
    #     dp[day][absent][late]
    #     """

    #     dp = [[0, 0, 0] for _ in range(2)]

    #     # initial state
    #     dp[0][0] = 1
    #     dp[0][1] = 1
    #     dp[1][0] = 1

    #     MOD = 10**9 + 7

    #     for i in range(1, n):
    #         new_dp = [[0, 0, 0] for _ in range(2)]
    #         new_dp[0][0] = (dp[0][0] + dp[0][1] + dp[0][2]) % MOD
    #         new_dp[0][1] = dp[0][0]
    #         new_dp[0][2] = dp[0][1]
    #         new_dp[1][0] = (
    #             dp[0][0] + dp[0][1] + dp[0][2] + dp[1][0] + dp[1][1] + dp[1][2]
    #         ) % MOD

    #         new_dp[1][1] = dp[1][0]
    #         new_dp[1][2] = dp[1][1]
    #         dp = new_dp

    #     summ = 0
    #     for i in range(2):
    #         for j in range(3):
    #             summ = (summ + dp[i][j]) % MOD

    #     return summ

    def checkRecord(self, n: int) -> int:
        # 4.Bottom-up DP: space optimization 2
        # time complexity: O(N)
        # space complexity: O(2*3*N)

        """
        dp[day][absent][late]
        """

        dp = [1, 1, 0, 1, 0, 0]

        MOD = 10**9 + 7

        for i in range(1, n):
            new_dp = [0, 0, 0, 0, 0, 0]

            new_dp[0] = (dp[0] + dp[1] + dp[2]) % MOD
            new_dp[1] = dp[0]
            new_dp[2] = dp[1]
            new_dp[3] = (dp[0] + dp[1] + dp[2] + dp[3] + dp[4] + dp[5]) % MOD

            new_dp[4] = dp[3]
            new_dp[5] = dp[4]
            dp = new_dp

        return sum(dp) % MOD


# @lc code=end
