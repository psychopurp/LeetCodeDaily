#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            tag = hash.get(nums[i], False)
            if tag is not False:
                return [tag, i]
            else:
                hash.setdefault(target-nums[i], i)

# @lc code=end


def twoSum(nums, target: int):
    hash = {}
    for i in range(len(nums)):
        tag = hash.get(nums[i], False)
        if tag is not False:
            return [tag, i]
        else:
            hash.setdefault(target-nums[i], i)


print(twoSum([2, 7, 11, 15], 9))
