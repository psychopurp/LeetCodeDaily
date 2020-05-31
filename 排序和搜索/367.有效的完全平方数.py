#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#

# @lc code=start


class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 <= num:
                l = mid + 1
            else:
                r = mid - 1
        return False


# @lc code=end
