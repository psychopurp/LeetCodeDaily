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
        result = []

        def backtrack(nums, track):
            if len(track) == len(nums):
                result.append(track[:])
                return

            for i in range(len(nums)):
                if nums[i] in track:
                    continue
                track.append(nums[i])
                backtrack(nums, track)
                track.pop()

        backtrack(nums, [])
        return result


# @lc code=end
