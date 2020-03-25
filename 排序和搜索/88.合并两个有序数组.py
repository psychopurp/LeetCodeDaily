#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        k = m + n-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        nums1[:j+1] = nums2[:j+1]

# @lc code=end


def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    N = m + n

    for k in reversed(range(N)):
        if j < 0:
            break
        if nums1[i] > nums2[j]:
            tmp = nums1[k]
            nums1[k] = nums1[i]
            nums1[i] = tmp
            if i > 1:
                i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1


merge([2, 0], 1, [1], 1)
