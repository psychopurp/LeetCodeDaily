#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def helper(index, track):
            if len(track) == len(digits):
                res.append(track)
                return

            for i in table[int(digits[index])]:
                helper(index+1, track+i)

        table = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
                 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        res = []
        helper(0, '')
        return res if len(digits) != 0 else []


# @lc code=end
