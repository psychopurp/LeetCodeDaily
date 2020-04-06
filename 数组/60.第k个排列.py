#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start


class Solution:
    # def getPermutation(self, n: int, k: int) -> str:
    #     result = []

    #     def backtrack(nums, track):
    #         if len(nums) == 0:
    #             result.append(track)
    #             return

    #         for i in range(len(nums)):
    #             backtrack(nums[:i] + nums[i + 1:], track + [nums[i]])
    #             if len(result) == k:
    #                 return
    #     nums = [i + 1 for i in range(n)]
    #     backtrack(nums, [])
    #     track_list = list(map(str, result[-1]))
    #     return ''.join(track_list)

    def getPermutation(self, n: int, k: int) -> str:
        track = []
        nums = [i + 1 for i in range(n)]

        def factorial(n):
            val = 1
            for i in range(n, 1, -1):
                val = val * i
            return val
        k = k-1
        while n > 0:
            tmp = k // factorial(n - 1)
            k = k % factorial(n-1)
            cur = nums[tmp]
            track.append(str(nums.pop(tmp)))
            n -= 1
        return ''.join(track)

# @lc code=end
