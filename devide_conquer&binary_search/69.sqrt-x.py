#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search solution
        # time complexity: O(log n)
        # space complexity: O(1)
        l, r = 0, x
        while l <= r:
            mid = (l+r)/2
            val = int(mid*mid)
            if val == x:
                return int(mid)

            if val < x:
                l = mid
            else:
                r = mid
# @lc code=end
