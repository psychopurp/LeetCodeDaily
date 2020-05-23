#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def backtrack(nums, visited, track):
            if len(track) == n:
                res.append(track[:])
                return

            for i in range(n):
                # 剪枝
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                    continue
                # 如果已经访问过 也跳过
                if visited[i]:
                    continue
                track.append(nums[i])
                visited[i] = True
                backtrack(nums, visited, track)
                visited[i] = False
                track.pop()


        res = []
        n = len(nums)
        if not nums:
            return res
        nums.sort()
        visited = [False for _ in range(n)]
        backtrack(nums, visited, [])
        return res

# @lc code=end
