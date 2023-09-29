#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] String to Integer (atoi)
#


# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        # Automation : State machine thingking
        # time complexity: O(N) N=len(s)
        # space complexity: O(1)
        STATE_START = "START"
        STATE_SIGNED = "+-"
        STATE_NUMBER = "NUM"

        INT_MIN = -(1 << 31)
        INT_MAX = (1 << 31) - 1

        cur_state = STATE_START
        num = 0
        sign = 1

        for i in range(len(s)):
            if cur_state == STATE_START:
                if s[i] == " ":
                    continue

                if s[i] == "+" or s[i] == "-":
                    cur_state = STATE_SIGNED
                    if s[i] == "-":
                        sign = -1
                    continue
                if "0" <= s[i] <= "9":
                    cur_state = STATE_NUMBER
                    num = num * 10 + ord(s[i]) - ord("0")
                    continue
            elif cur_state == STATE_SIGNED:
                if "0" <= s[i] <= "9":
                    cur_state = STATE_NUMBER
                    num = num * 10 + ord(s[i]) - ord("0")
                    continue
            elif cur_state == STATE_NUMBER:
                if s[i] == "." or s[i] == " " or s[i] < "0" or s[i] > "9":
                    return sign * num

                if "0" <= s[i] <= "9":
                    num = num * 10 + ord(s[i]) - ord("0")

                    if sign * num < INT_MIN:
                        return INT_MIN

                    if sign * num > INT_MAX:
                        return INT_MAX

                    continue
            return 0

        return sign * num


# @lc code=end
