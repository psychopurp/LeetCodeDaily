#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # binary search
        # time complexity: O(N*logN)
        # space complexity: O(1)

        def count_range(end: int) -> int:
            count = 0
            for num in nums:
                if num <= end:
                    count += 1
            return count

        l, r = 1, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            count = count_range(mid)
            if l==r and count>1:
                return l
            
            if count > mid:
                r = mid
            else:
                l = mid+1


# @lc code=end
