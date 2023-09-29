#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] Length of Last Word
#


# @lc code=start
class Solution:
    # def lengthOfLastWord(self, s: str) -> int:
    #     # 1. Use the language api
    #     # time complexity: O(N)
    #     # space complexity: O(N) N=len(s)
    #     return len(s.split()[-1])

    def lengthOfLastWord(self, s: str) -> int:
        # 2. Iterate s from back to start
        # time complexity: O(N)
        # space complexity: O(1)

        count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                count += 1
            elif count > 0:
                break

        return count


# @lc code=end
