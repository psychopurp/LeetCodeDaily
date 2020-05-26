#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        from collections import deque
        size, general_dict = len(start), {}
        for word in bank:
            for i in range(size):
                template = word[:i] + '*' + word[i + 1:]
                general_dict[template] = general_dict.get(
                    template, []) + [word]

        queue = deque()
        queue.append((start, 0))
        visited = set()
        while queue:
            word, level = queue.popleft()
            if word == end:
                return level
            if word in visited:
                continue
            visited.add(word)
            for i in range(size):
                template = template = word[:i] + '*' + word[i + 1:]
                for item in general_dict.get(template, []):
                    if item not in visited:
                        queue.append((item, level+1))
        return -1

# @lc code=end
