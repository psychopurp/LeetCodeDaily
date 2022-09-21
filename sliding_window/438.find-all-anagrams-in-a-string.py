#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] Find All Anagrams in a String
#

# @lc code=start
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # sliding window
        # time complexity: O(n)
        # space complexity: O(n)

        from collections import defaultdict

        window = defaultdict(int)
        for c in p:
            window[c] += 1

        left = right = match = 0
        ans = []

        while right < len(s):
            window[s[right]] -= 1

            if window[s[right]] >= 0:
                match += 1

            if right-left+1 == len(p):
                if match == len(p):
                    ans.append(left)

                window[s[left]] += 1
                if window[s[left]] > 0:
                    match -= 1

                left += 1
            right += 1

        return ans


# @lc code=end
