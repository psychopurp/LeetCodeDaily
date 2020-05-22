#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start


class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     # 回溯算法
    #     result = []

    #     def backtrack(nums, track):
    #         if len(nums) == 0:
    #             result.append(track)

    #         for i in range(len(nums)):
    #             backtrack(nums[:i]+nums[i+1:], track+[nums[i]])

    #     backtrack(nums, [])
    #     return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 回溯算法
        def back_track(nums, track):
            if len(nums) == len(track):
                res.append(track)
                return

            for i in nums:
                if i in track:
                    continue
                back_track(nums, track+[i])

        res = []
        back_track(nums, [])
        return res


# @lc code=end
