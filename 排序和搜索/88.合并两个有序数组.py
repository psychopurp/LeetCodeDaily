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
        cur = m+n-1
        n1 = m-1
        n2 = n-1
        while n2 >= 0:
            if n1 < 0:
                nums1[cur] = nums2[n2]
                n2 -= 1
            elif nums1[n1] >= nums2[n2]:
                nums1[cur], nums1[n1] = nums1[n1], nums1[cur]
                n1 -= 1
            else:
                nums1[cur] = nums2[n2]
                n2 -= 1
            cur -= 1

    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     # 双指针
    #     i, j = m-1, n-1
    #     for k in reversed(range(m+n)):
    #         if i < 0:
    #             nums1[k] = nums2[j]
    #             j -= 1
    #             continue
    #         if j < 0:
    #             break
    #         if nums1[i] > nums2[j]:
    #             val = nums1[i]
    #             i -= 1
    #         else:
    #             val = nums2[j]
    #             j -= 1
    #         nums1[k] = val

# @lc code=end


# def merge(nums1, m, nums2, n):
#     i = m - 1
#     j = n - 1
#     N = m + n

#     for k in reversed(range(N)):
#         if j < 0:
#             break
#         if nums1[i] > nums2[j]:
#             tmp = nums1[k]
#             nums1[k] = nums1[i]
#             nums1[i] = tmp
#             if i > 1:
#                 i -= 1
#         else:
#             nums1[k] = nums2[j]
#             j -= 1


# merge([2, 0], 1, [1], 1)
