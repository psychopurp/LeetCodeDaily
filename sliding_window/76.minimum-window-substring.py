#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     # 1. sliding window
    #     # time complexity: O(m) m=len(s) n=len(t)
    #     # space complexity: O(m+n)

    #     from collections import defaultdict
    #     ht = defaultdict(int)
    #     hw = defaultdict(int)

    #     begin = end = match = 0
    #     min_window = ""

    #     # initialize ht
    #     for c in t:
    #         ht[c] += 1

    #     while end < len(s):
    #         hw[s[end]] += 1

    #         if hw[s[end]] <= ht[s[end]]:
    #             match += 1

    #         # shrink
    #         while begin < end and hw[s[begin]] > ht[s[begin]]:
    #             hw[s[begin]] -= 1
    #             begin += 1

    #         if match == len(t):
    #             if not min_window or end-begin+1 < len(min_window):
    #                 min_window = s[begin:end+1]

    #         end += 1
    #     return min_window

    def minWindow(self, s: str, t: str) -> str:
        # 2. sliding window
        # time complexity: O(m) m=len(s) n=len(t)
        # space complexity: O(m+n)

        from collections import defaultdict

        begin = end = match = 0
        min_window = ""
        ht = defaultdict(int)

        for c in t:
            ht[c] += 1

        while end < len(s):

            ht[s[end]] -= 1

            if ht[s[end]] >= 0:
                match += 1

            while match == len(t):
                if not min_window or end-begin+1 < len(min_window):
                    min_window = s[begin:end+1]

                ht[s[begin]] += 1

                if ht[s[begin]] > 0:
                    match -= 1

                begin += 1
            end+=1
            
        return min_window

# @lc code=end
