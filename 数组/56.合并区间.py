#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 时间复杂度O(nlogn) 主要花费在排序上
        intervals.sort(key=lambda x: x[0])
        merged = []

        for i in intervals:
            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)
                continue
            if merged[-1][-1] >= i[0]:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged
        # @lc code=end
