#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start


class Solution:
    # def findLengthOfLCIS(self, nums: List[int]) -> int:
    #     slow = 0
    #     fast = slow
    #     count = 0
    #     while slow < len(nums):
    #         while fast+1 < len(nums):
    #             if nums[fast + 1] > nums[fast]:
    #                 fast += 1
    #                 continue
    #             else:
    #                 break
    #         if fast - slow + 1 > count:
    #             count = fast - slow + 1
    #         slow = fast + 1
    #         fast = slow
    #     return count

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # 滑动窗口
        max_count = 0
        tmp_count = 1
        if not nums:
            return 0

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                tmp_count += 1
                continue
            else:
                max_count = max(max_count, tmp_count)
                tmp_count = 1
                continue
        return max(max_count, tmp_count)


# @lc code=end
