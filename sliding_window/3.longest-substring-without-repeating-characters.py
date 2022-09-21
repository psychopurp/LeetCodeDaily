#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        # time complexity: O(2*n)
        # space complexity: O(n)

        from collections import defaultdict
        begin = end = 0

        hw = defaultdict(int)
        max_win = 0

        while end < len(s):
            hw[s[end]] += 1

            while hw[s[end]] > 1:
                hw[s[begin]] -= 1
                begin += 1

            max_win = max(max_win, end-begin+1)
            end += 1
        return max_win


# @lc code=end
