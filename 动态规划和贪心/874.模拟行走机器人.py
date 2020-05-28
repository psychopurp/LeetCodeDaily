#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction = {
            "up": [0, 1, "right", "left"],
            "down": [0, -1, "left", "right"],
            "left": [-1, 0, "up", "down"],
            "right": [1, 0, "down", "up"]
        }
        x = y = 0
        direct = "up"

        obstacles = set(map(tuple, obstacles))
        res = 0
        for com in commands:
            if com > 0:
                for step in range(com):
                    if (x + direction[direct][0], y + direction[direct][1]) not in obstacles:
                        x += direction[direct][0]
                        y += direction[direct][1]
                        res = max(res, x**2+y**2)
            elif com == -1:
                direct = direction[direct][2]
            else:
                direct = direction[direct][3]
        return res

# @lc code=end
