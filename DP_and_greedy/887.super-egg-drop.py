#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] Super Egg Drop
#


# @lc code=start
class Solution:
    # def superEggDrop(self, k: int, n: int) -> int:
    #     # 1.DP solution, this will TLE
    #     # time complexity: O(N^2*K)
    #     # space complexity: O(N*K)
    #     '''
    #     dp[n][k] means that given k eggs and n moves, what is the minimum number of moves for checking the floor which will break the egg
    #     '''

    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int, k: int) -> int:
    #         if i == 0:
    #             return 0
    #         if k == 1:
    #             return i

    #         min_attempts = float("inf")
    #         for j in range(1, i + 1):
    #             # if egg is broken at j, it will be: dp[j][k] = dp[j-1][k-1] + 1
    #             # if egg is not broken at j, it will be: dp[j][k] = dp[i-j][k] +1
    #             broken = dp(j - 1, k - 1)
    #             not_broken = dp(i - j, k)

    #             # chose the worst case
    #             current_attempts = 1 + max(broken, not_broken)
    #             # select the best case from the worst cases
    #             min_attempts = min(min_attempts, current_attempts)

    #         return min_attempts

    #     return dp(n, k)

    # def superEggDrop(self, k: int, n: int) -> int:
    #     # 2.DP solution with binary search optimization, this will success
    #     # time complexity: O(K*N*logN) time complexity will be optimized to O(log N) from O(N) by using binary search
    #     # space complexity: O(N*K)

    #     """
    #     dp[n][k] means that given k eggs and n moves, what is the minimum number of moves for checking the floor which will break the egg
    #     """

    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int, k: int) -> int:
    #         if i == 0:
    #             return 0
    #         if k == 1:
    #             return i

    #         # this idea is important!
    #         # find the crossing point of dp(x-1,k-1) and dp(n-x,k)
    #         l, r = 1, i + 1
    #         while l <= r:
    #             # if egg is broken at j, it will be: dp[j][k] = dp[j-1][k-1] + 1
    #             # if egg is not broken at j, it will be: dp[j][k] = dp[i-j][k] +1

    #             j = (l + r) >> 1
    #             broken = dp(j - 1, k - 1)
    #             not_broken = dp(i - j, k)
    #             if broken < not_broken:
    #                 l = j + 1
    #             else:
    #                 r = j - 1

    #         mid = l
    #         return 1 + max(dp(mid - 1, k - 1), dp(i - mid, k))

    #     return dp(n, k)

    # def superEggDrop(self, k: int, n: int) -> int:
    #     # 3.Another DP solution : Top-Down DP
    #     # time complexity: O(K*logN)
    #     # space complexity: O(N*K)

    #     """
    #     this DP thinking is different than previous solutions!
    #     dp[m][k] represents the maximum number of floors that can be "guaranteed" by moving m steps with k eggs.

    #     explanation for this:
    #     1. https://leetcode.com/problems/super-egg-drop/solutions/158974/c-java-python-2d-and-1d-dp-o-klogn/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china
    #     2. https://leetcode.cn/problems/super-egg-drop/solutions/7459/ji-dan-diao-luo-xiang-jie-by-shellbye/
    #     """

    #     from functools import lru_cache

    #     @lru_cache(None)
    #     def dp(i: int, k: int) -> int:
    #         if i == 0:
    #             return 0
    #         if k == 1:
    #             return i

    #         return 1 + dp(i - 1, k - 1) + dp(i - 1, k)

    #     for i in range(1, n + 1):
    #         if dp(i, k) >= n:
    #             return i

    # def superEggDrop(self, k: int, n: int) -> int:
    #     # 4.DP solution: Bottom-up DP, optimize solution 3
    #     # time complexity: O(K*logN)
    #     # space complexity: O(N*K)

    #     """
    #     This DP thinking is different than previous solutions!
    #     dp[m][k] represents the maximum number of floors that can be "guaranteed" by moving m steps with k eggs.

    #     Explanation for this:
    #     1. https://leetcode.com/problems/super-egg-drop/solutions/158974/c-java-python-2d-and-1d-dp-o-klogn/?utm_source=LCUS&utm_medium=ip_redirect&utm_campaign=transfer2china

    #     For the reason why time complexity leads to O(logN):
    #     #1:
    #     If we only have 1 egg to check 100 floors, you will do 100 moves
    #     if we have 100 eggs to check 100 floors, you will have binary search in your mind, this is where log come in.

    #     #2:
    #     In the sample code Lee provided, the loop ends when dp[M][K] >= N. don't confuse this as when M reaches N.

    #     #3:
    #     dp[m][k] = dp[m-1][k-1] + 1 + dp[m-1][k]
    #     for DP transition suggests that we use 1 move to check some floor. Based on the result, we either use remaining eggs to check floors below (when egg breaks), or use all eggs to check floors above (when it did not break). This divide divide-and-conquer pattern leads to O(logN)
    #     """

    #     dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    #     for i in range(1, n + 1):
    #         for j in range(1, k + 1):
    #             dp[i][j] = 1 + dp[i - 1][j - 1] + dp[i - 1][j]
    #             if dp[i][j] >= n:
    #                 return i

    def superEggDrop(self, k: int, n: int) -> int:
        # 5.DP solution: Bottom-up DP, optimize solution 4, turn 2D array DP to 1D
        # time complexity: O(min(K,logN))
        # space complexity: O(K)

        dp = [0 for _ in range(k + 1)]

        for i in range(1, n + 1):
            prev = 0
            for j in range(1, k + 1):
                tmp = dp[j]
                dp[j] = 1 + dp[j] + prev
                prev = tmp
                if dp[j] >= n:
                    return i


# @lc code=end
