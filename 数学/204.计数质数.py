#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        # 厄拉多塞筛法 Sieve of Eratosthenes
        # 时间复杂度O(N * loglogN)
        isPrime = [True for i in range(n)]
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
                for j in range(i*i, n, i):
                    isPrime[j] = False
        return count

# @lc code=end
