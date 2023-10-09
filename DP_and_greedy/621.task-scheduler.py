#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from typing import Dict, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Bucket thought: https://leetcode.cn/problems/task-scheduler/solutions/196302/tong-zi-by-popopop/
        # time complexity: O(N)
        # space complexity: O(N)
        """
        ## RC ##
        ## APPROACH : HASHMAP ##
        ## LOGIC : TAKE THE MAXIMUM FREQUENCY ELEMENT AND MAKE THOSE MANY NUMBER OF SLOTS ##
        ##  Slot size = (n+1) if n= 2 => slotsize = 3 Example: {A:5, B:1} => ABxAxxAxxAxxAxx => indices of A = 0,2 and middle there should be n elements, so slot size should be n+1

        ## Ex: {A:6,B:4,C:2} n = 2
        ## final o/p will be
        ## slot size / cycle size = 3
        ## Number of rows = number of A's (most freq element)
        # [
        #     [A, B,      C],
        #     [A, B,      C],
        #     [A, B,      idle],
        #     [A, B,      idle],
        #     [A, idle,   idle],
        #     [A   -        - ],
        # ]
        #
        # so from above total time intervals = (max_freq_element - 1) * (n + 1) + (all elements with max freq)
                                     # ans   =     rows_except_last   * columns +        last_row


        ## but consider {A:5, B:1, C:1, D:1, E:1, F:1, G:1, H:1, I:1, J:1, K:1, L:1} n = 1
        ## total time intervals by above formula will be 4 * 2 + 1 = 9, which is less than number of elements, which is not possible. so we have to return max(ans, number of tasks)

        """

        from collections import defaultdict

        counter = defaultdict(int)
        max_task = 0
        for task in tasks:
            counter[task] += 1
            max_task = max(max_task, counter[task])

        count_max_task = 0
        for key in counter:
            if counter[key] == max_task:
                count_max_task += 1

        return max(len(tasks), (max_task - 1) * (n + 1) + count_max_task)


# @lc code=end
