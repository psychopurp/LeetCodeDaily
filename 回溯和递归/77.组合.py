#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def backtrack(level, track):
            if level == k:
                res.append(track)
                return
            start = track[-1] if track else 0
            for i in range(start+1, n + 1):
                if i not in track:
                    backtrack(level+1, track+[i])

        res = []
        backtrack(0, [])
        return res


# @lc code=end
