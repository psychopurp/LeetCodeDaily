#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 摩尔投票法 时间复杂度 O(N) 空间复杂度O(1)
        count = 0
        candidate = 0
        for x in nums:
            if count == 0:
                candidate = x
                count += 1
            elif candidate == x:
                count += 1
            else:
                count -= 1
        return candidate

# @lc code=end
