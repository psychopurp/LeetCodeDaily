#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # time complexity: O(m+n)
        # space complexity: O(1)
        idx = m+n-1
        while n:
            if m and nums1[m-1] > nums2[n-1]:
                nums1[idx] = nums1[m-1]
                m -= 1
            else:
                nums1[idx] = nums2[n-1]
                n -= 1
            idx -= 1
# @lc code=end
