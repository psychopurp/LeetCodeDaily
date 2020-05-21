#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque使用 时间复杂度O(N+K) 空间复杂度O(K)
        from collections import deque
        d = deque()
        res = []

        for i, val in enumerate(nums):
            while d and val > nums[d[-1]]:
                d.pop()
            d.append(i)

            if i - d[0] == k:
                d.popleft()

            if i + 1 >= k:
                res.append(nums[d[0]])
        return res


# @lc code=end
