#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        from collections import deque
        size, general_dict = len(beginWord), {}
        for word in wordList:
            for i in range(size):
                template = word[:i] + '*' + word[i + 1:]
                general_dict[template] = general_dict.get(
                    template, []) + [word]

        queue = deque()
        queue.append((beginWord, 0))
        visited = set()
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level+1
            if word in visited:
                continue
            visited.add(word)
            for i in range(size):
                template = template = word[:i] + '*' + word[i + 1:]
                for item in general_dict.get(template, []):
                    if item not in visited:
                        queue.append((item, level+1))
        return 0


# @lc code=end
