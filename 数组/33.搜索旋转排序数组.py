#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return - 1
        n = len(nums)

        # 找出旋转的点
        def findMin():
            begin = 0
            end = n - 1
            if nums[begin] <= nums[end]:
                return 0
            while begin < end:
                if end - begin == 1:
                    return end
                mid = (begin + end) // 2
                if nums[mid] < nums[begin]:
                    end = mid
                    continue
                if nums[mid] > nums[end]:
                    begin = mid
                    continue

        def binarySearch(begin, end):
            if begin >= end:
                if target == nums[begin]:
                    return begin
                else:
                    return -1
            mid = (begin + end) // 2
            if target <= nums[mid]:
                return binarySearch(begin, mid)
            else:
                return binarySearch(mid+1, end)

        min_index = findMin()
        if min_index == 0:
            if nums[0] <= target <= nums[n-1]:
                return binarySearch(0, n - 1)
            else:
                return -1
        elif nums[0] <= target <= nums[min_index - 1]:
            return binarySearch(0, min_index - 1)
        elif nums[min_index] <= target <= nums[len(nums) - 1]:
            return binarySearch(min_index, len(nums)-1)
        else:
            return -1
# @lc code=end
