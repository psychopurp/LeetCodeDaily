#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start

class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     # brute force solution
    #     # time complexity: O(n*k)
    #     # space complexity: O(1)
    #     ans = []
    #     for i in range(len(nums)):
    #         if i+k <= len(nums):
    #             ans.append(max(nums[i:i+k]))

    #     return ans

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic queue
        # time complexity: O(n)
        # space complexity: O(k)

        import collections

        d = collections.deque()
        ans = []

        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]:
                d.pop()

            d.append(i)

            if i-k == d[0]:
                d.popleft()

            if i >= k-1:
                ans.append(nums[d[0]])

        return ans
# @lc code=end
