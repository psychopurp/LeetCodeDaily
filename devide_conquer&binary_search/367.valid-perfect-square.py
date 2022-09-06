#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    #     # binary search
    #     # time complexity: O(log N)
    #     # space complexity: O(1)

    #     l, r = 1, num
    #     while l <= r:
    #         mid = (l+r)//2
    #         val = mid*mid
    #         if val == num:
    #             return True
    #         elif val < num:
    #             l = mid+1
    #         else:
    #             r = mid-1

    #     return False

    def isPerfectSquare(self, num: int) -> bool:
        # linear solution
        # time complexity: O(n)
        # space complexity: O(1)

        val = 1

        while val*val <= num:
            if val*val == num:
                return True
            else:
                val += 1
        return False


# @lc code=end
