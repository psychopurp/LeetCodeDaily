#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        num_set = set(nums)
        for i in num_set:
            # 从作为连续序列的第一个数字去找对应的最长序列
            if i - 1 not in num_set:
                cur_num = i
                tmp_count = 1
                while cur_num + 1 in num_set:
                    tmp_count += 1
                    cur_num += 1
                max_count = max(tmp_count, max_count)
        return max_count


# @lc code=end
