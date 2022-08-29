#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] Walking Robot Simulation
#

# @lc code=start
from typing import Dict, List, Tuple


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # greedy solution
        # time complexity: O(M*N) M=len(commands) N=len(obstacles)
        # space complexity: O(N) used in set

        directions: Dict[str, Tuple[int, int]] = {
            "up": (0, 1),
            "right": (1, 0),
            "down": (0, -1),
            "left": (-1, 0),
        }

        change: Dict[str, Dict[int, str]] = {
            "up": {-1: "right", -2: "left"},
            "right": {-1: "down", -2: "up"},
            "down": {-1: "left", -2: "right"},
            "left": {-1: "up", -2: "down"},
        }

        cur_direction = "up"
        cur_pos = [0, 0]
        obs = set(map(tuple, obstacles))
        max_val = 0

        for command in commands:
            if command < 0:
                cur_direction = change[cur_direction][command]
            else:
                dx, dy = directions[cur_direction]
                for _ in range(command):
                    if (cur_pos[0]+dx, cur_pos[1]+dy) in obs:
                        break
                    cur_pos[0] += dx
                    cur_pos[1] += dy

                max_val = max(max_val, cur_pos[0] ** 2+cur_pos[1] ** 2)

        return max_val
# @lc code=end
