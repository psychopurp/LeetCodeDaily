#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from typing import List


class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    #     # nums = [1,2,3,4,5,6,7], k = 3
    #     # reverse step 1: [7,6,5,4,3,2,1]
    #     # reverse step 2: [5,6,7,4,3,2,1]
    #     # reverse step 3: [5,6,7,1,2,3,4]
    #     # time complexity: O(n)
    #     # space complexity: O(1)
    #     def reverse(left: int, right: int):
    #         while left < right:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1

    #     k = k % len(nums)
    #     reverse(0, len(nums)-1)
    #     reverse(0, k-1)
    #     reverse(k, len(nums)-1)

    def rotate(self, nums: List[int], k: int) -> None:
        # time complexity: O(n)
        # space complexity: O(1)

        i = 0
        count = 0
        while count < len(nums):
            cur = i
            curNum = nums[i]
            while count < len(nums):
                nextPos = (cur+k) % len(nums)
                nextNum = nums[nextPos]
                nums[nextPos] = curNum
                cur = nextPos
                curNum = nextNum
                count += 1
                if nextPos == i:
                    i += 1
                    break


# @lc code=end
