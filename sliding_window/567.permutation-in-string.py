#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # sliding window
        # time complexity: O(n)
        # space complexity: O(n)

        from collections import defaultdict

        window = defaultdict(int)

        for c in s1:
            window[c] += 1

        left = right = match = 0

        while right < len(s2):
            window[s2[right]] -= 1

            if window[s2[right]] >= 0:
                match += 1

            if right-left+1 == len(s1):
                if match == len(s1):
                    return True

                window[s2[left]] += 1
                if window[s2[left]] > 0:
                    match -= 1
                left += 1

            right += 1

        return False


# @lc code=end
