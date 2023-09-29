#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] Reverse Words in a String
#


# @lc code=start
class Solution:
    # def reverseWords(self, s: str) -> str:
    #     # 1.Use language api
    #     # time complexity: O(N) N=len(s)
    #     # space complexity: O(N)
    #     words = s.split()
    #     words.reverse()
    #     return " ".join(words)

    def reverseWords(self, s: str) -> str:
        # 2. two-pointers: iterate from right
        # time complexity: O(N) N=len(s)
        # space complexity: O(N)

        ans = []
        right = -1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if right != -1 and right - i > 0:
                    ans.append(s[i + 1 : right + 1])
                    right = -1
                continue

            if right == -1:
                right = i

        if right != -1:
            ans.append(s[: right + 1])

        return " ".join(ans)


# @lc code=end
