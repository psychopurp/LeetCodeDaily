#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List


class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     # hash map
    #     # time complexity: O(n)
    #     # space complexity: O(n)

    #     hash = {}
    #     for num in nums:
    #         hash[num] = hash.get(num, 0)+1
    #         if hash[num] > len(nums)//2:
    #             return num

    # def majorityElement(self, nums: List[int]) -> int:
    #     # Boyer-Moore algorithm
    #     # time complexity: O(n)
    #     # space complexity: O(1)

    #     candidate = None
    #     vote = 0
    #     for num in nums:
    #         if vote == 0:
    #             candidate = num

    #         if candidate == num:
    #             vote += 1
    #         else:
    #             vote -= 1
    #     return candidate

    def majorityElement(self, nums: List[int]) -> int:
        # devide and conquer
        # time complexity: O(N*logN)
        # space complexity: O(logN)

        def getMajorityElement(left: int, right: int) -> int:

            if left == right:
                return nums[left]

            mid = (left+right)//2

            leftMajirity = getMajorityElement(left, mid)
            rightMajority = getMajorityElement(mid+1, right)

            if leftMajirity == rightMajority:
                return leftMajirity

            leftCount = sum(1 for i in range(left, right+1)
                            if nums[i] == leftMajirity)
            rightCount = sum(1 for i in range(left, right+1)
                             if nums[i] == rightMajority)

            return leftMajirity if leftCount > rightCount else rightMajority

        return getMajorityElement(0, len(nums)-1)

# @lc code=end
