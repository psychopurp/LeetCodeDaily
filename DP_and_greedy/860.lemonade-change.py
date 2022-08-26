#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] Lemonade Change
#

# @lc code=start
from typing import Dict, List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # greedy algorithm : use up the large coins first
        # time complexity: O(N)
        # space complexity: O(1)
        count: Dict[int, int] = {5: 0, 10: 0}

        for bill in bills:
            if bill == 5:
                count[5] += 1

            if bill == 10:
                if count[5] == 0:
                    return False
                count[10] += 1
                count[5] -= 1

            if bill == 20:
                if count[10] > 0 and count[5] > 0:
                    count[10] -= 1
                    count[5] -= 1
                elif count[5] >= 3:
                    count[5] -= 3
                else:
                    return False
        return True
# @lc code=end
