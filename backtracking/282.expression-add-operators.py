#
# @lc app=leetcode.cn id=282 lang=python3
#
# [282] Expression Add Operators
#

# @lc code=start
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        # backtracking
        # Time Complexity: O(4^n)
        # Space Complexity: O(n)
        def backtrack(index: int, cur_path: str, cur_val: int, last_item_val: int):
            if index == len(num):
                if cur_val == target:
                    result.append(cur_path)
                return

            for i in range(index, len(num) + 1):
                val_str = num[index: i + 1]
                if not val_str:
                    continue

                if len(val_str) > 1 and val_str[0] == "0":
                    return

                if cur_path == "":
                    backtrack(i + 1, val_str, cur_val +
                              int(val_str), int(val_str))
                else:
                    backtrack(i + 1, cur_path + "+" +
                              val_str, cur_val+int(val_str), int(val_str))
                    backtrack(i + 1, cur_path + "-" +
                              val_str, cur_val-int(val_str), -int(val_str))
                    backtrack(i + 1, cur_path + "*" +
                              val_str, (cur_val-last_item_val) + last_item_val*int(val_str), last_item_val*int(val_str))

        result = []
        backtrack(0, "", 0, 0)
        return result


# @lc code=end
