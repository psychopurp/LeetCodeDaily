#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start


class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     # nums 的每一位可选可不选

    #     def helper(track, index):
    #         if index == len(nums):
    #             res.append(track[:])
    #             return

    #         helper(track, index + 1)
    #         track.append(nums[index])
    #         helper(track, index + 1)
    #         track.pop()

    #     res = []
    #     helper([], 0)
    #     return res

    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 这种写法得再练练
        sub = [[]]

        for num in nums:
            newSet = []
            for i in sub:
                newSet.append(i + [num])
            sub.extend(newSet)
        return sub


# @lc code=end
