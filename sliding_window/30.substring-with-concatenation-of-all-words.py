#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List


class Solution:
    # def findSubstring(self, s: str, words: List[str]) -> List[int]:
    #     # 1.sliding window
    #     # time complexity: O(m*n) m=len(s) n=len(words)
    #     # space complexity: O(n)

    #     from collections import defaultdict
    #     window = defaultdict(int)

    #     for word in words:
    #         window[word] += 1

    #     left = right = match = 0
    #     ans = []

    #     m, n = len(words), len(words[0])

    #     while right+n <= len(s):
    #         cur_word = s[right:right+n]

    #         window[cur_word] -= 1
    #         if window[cur_word] >= 0:
    #             match += 1

    #             if match != len(words):
    #                 right += n
    #                 continue

    #         if match == len(words):
    #             ans.append(left)

    #         # reset current match and start from left+1
    #         match = 0
    #         i = left
    #         while i <= right:
    #             window[s[i:i+n]] += 1
    #             i += n

    #         left += 1
    #         right = left

    #     return ans

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # 2.sliding window
        # time complexity: O(wl*n) wl=len(words[0]) n=len(s)
        # space complexity: O(n)

        from collections import defaultdict

        window = defaultdict(int)
        for word in words:
            window[word] += 1

        match = 0
        m, n = len(words), len(words[0])
        ans = []

        for i in range(n):
            left = right = i
            match = 0

            # single sliding window:O(len(s))
            while right+n <= len(s):
                cur_word = s[right:right+n]
                window[cur_word] -= 1
                if window[cur_word] >= 0:
                    match += 1

                # shrink
                if right+n-left == m*n:
                    if match == m:
                        ans.append(left)

                    window[s[left:left+n]] += 1
                    if window[s[left:left+n]] > 0:
                        match -= 1
                    left += n

                right += n

            # reset the window
            while left <= right:
                window[s[left:left+n]] += 1
                left += n
        return ans

# @lc code=end
