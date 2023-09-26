#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from typing import Dict, List


class Solution:
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     # BFS: 1.one-end BFS
    #     # time complexity: O(N*C^2) N=len(wordList) C=len(word)
    #     # space complexity: O(N*C^2)

    #     from collections import deque

    #     patterns: Dict[str, List[str]] = {}
    #     for word in wordList:
    #         for i, _ in enumerate(word):
    #             template = word[:i]+"*"+word[i+1:]
    #             patterns.setdefault(template, []).append(word)

    #     q = deque()
    #     q.append((beginWord, 1))
    #     visited = set()

    #     while q:
    #         word, step = q.popleft()
    #         for i, _ in enumerate(word):
    #             template = word[:i]+"*"+word[i+1:]

    #             for item in patterns.get(template, []):
    #                 if word == endWord:
    #                     return step
    #                 if item not in visited:
    #                     q.append((item, step+1))
    #                     visited.add(word)

    #     return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     # BFS: 2.two-end BFS
    #     # time complexity: O(N*C^2) N=len(wordList) C=len(word)
    #     # space complexity: O(N*C^2)

    #     from collections import deque

    #     if endWord not in wordList:
    #         return 0

    #     patterns: Dict[str, List[str]] = {}
    #     for word in wordList:
    #         for i, _ in enumerate(word):
    #             template = word[:i]+"*"+word[i+1:]
    #             patterns.setdefault(template, []).append(word)

    #     q1 = deque([(beginWord, 1)])
    #     q2 = deque([(endWord, 1)])

    #     visited1 = {beginWord: 1}
    #     visited2 = {endWord: 1}

    #     def update(word: str, step: int, q: deque, visited1: Dict[str, int], visited2: Dict[str, int]) -> int:
    #         for i, _ in enumerate(word):
    #             template = word[:i]+"*"+word[i+1:]
    #             for item in patterns.get(template, []):
    #                 if item in visited2:
    #                     return step+visited2[item]
    #                 if item not in visited1:
    #                     visited1[item] = step+1
    #                     q.append((item, step+1))
    #         return 0

    #     while q1 and q2:
    #         for _ in range(len(q1)):
    #             word, step = q1.popleft()
    #             ret = update(word, step, q1, visited1, visited2)
    #             if ret:
    #                 return ret

    #         for _ in range(len(q2)):
    #             word, step = q2.popleft()
    #             ret = update(word, step, q2, visited2, visited1)
    #             if ret:
    #                 return ret

    #     return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     # BFS 3.one-end BFS
    #     # time complexity: O(N*C^2) N=len(wordList) C=len(word)
    #     # space complexity: O(N*C)

    #     from collections import deque

    #     q = deque([(beginWord, 1)])
    #     visited = set([beginWord])
    #     wordList = set(wordList)

    #     alph = "abcdefghijklmnopqrstuvwxyz"

    #     if endWord not in wordList:
    #         return 0

    #     while q:
    #         for _ in range(len(q)):
    #             word, step = q.popleft()

    #             for i in range(len(word)):
    #                 for c in alph:
    #                     newWord = word[:i]+c+word[i+1:]
    #                     if newWord in wordList and newWord not in visited:
    #                         if newWord == endWord:
    #                             return step+1
    #                         q.append((newWord, step+1))
    #                         visited.add(newWord)

    #     return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     # BFS: 4.two-end BFS imporved based on two-end solution 2
    #     # time complexity: O(N*C^2) N=len(wordList) C=len(word)
    #     # space complexity: O(N*C^2)

    #     from collections import deque

    #     if endWord not in wordList:
    #         return 0

    #     patterns: Dict[str, List[str]] = {}
    #     for word in wordList:
    #         for i, _ in enumerate(word):
    #             template = word[:i]+"*"+word[i+1:]
    #             patterns.setdefault(template, []).append(word)

    #     q1 = deque([(beginWord, 1)])
    #     q2 = deque([(endWord, 1)])

    #     visited1 = {beginWord: 1}
    #     visited2 = {endWord: 1}

    #     def update(word: str, step: int, q: deque, visited1: Dict[str, int], visited2: Dict[str, int]) -> int:
    #         for i, _ in enumerate(word):
    #             template = word[:i]+"*"+word[i+1:]
    #             for item in patterns.get(template, []):
    #                 if item in visited2:
    #                     return step+visited2[item]
    #                 if item not in visited1:
    #                     visited1[item] = step+1
    #                     q.append((item, step+1))
    #         return 0

    #     while q1 and q2:
    #         # search the shortest end first
    #         if len(q2) < len(q1):
    #             q1, q2 = q2, q1
    #             visited1, visited2 = visited2, visited1

    #         for _ in range(len(q1)):
    #             word, step = q1.popleft()
    #             ret = update(word, step, q1, visited1, visited2)
    #             if ret:
    #                 return ret

    #     return 0

    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     # BFS: 5.one-end bfs implementation with time improvement by can_change function
    #     # time complexity: O(N*C) N=len(wordList) C=len(word)
    #     # space complexity: O(N*C)
    #     from collections import deque

    #     def can_change(word1: str, word2: str) -> bool:
    #         if len(word1) != len(word2):
    #             return False

    #         diff = 0
    #         for i in range(len(word1)):
    #             if word1[i] != word2[i]:
    #                 diff += 1

    #             if diff > 1:
    #                 return False

    #         return diff == 1

    #     visited = set([beginWord])
    #     q = deque()
    #     q.append(beginWord)
    #     level = 0

    #     while q:
    #         level += 1
    #         for _ in range(len(q)):
    #             word = q.popleft()
    #             if word == endWord:
    #                 return level

    #             for next_word in wordList:
    #                 if next_word not in visited and can_change(word, next_word):
    #                     visited.add(next_word)
    #                     q.append(next_word)

    #     return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS: 6.two-end bfs implementation with time improvement by can_change function
        # time complexity: O(N*C) N=len(wordList) C=len(word)
        # space complexity: O(N*C)

        if endWord not in wordList:
            return 0

        from collections import deque

        def can_change(word1: str, word2: str) -> bool:
            if len(word1) != len(word2):
                return False

            diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    diff += 1

                if diff > 1:
                    return False

            return diff == 1

        q_start, q_end = deque([beginWord]), deque([endWord])
        visited_start, visited_end = set([beginWord]), set([endWord])

        level = 0

        while q_start and q_end:
            if len(q_end) < len(q_start):
                q_start, q_end = q_end, q_start
                visited_start, visited_end = visited_end, visited_start

            level += 1
            for _ in range(len(q_start)):
                word = q_start.popleft()
                if word in visited_end:
                    return level

                for next_word in wordList:
                    if next_word not in visited_start and can_change(word, next_word):
                        visited_start.add(next_word)
                        q_start.append(next_word)

        return 0


# @lc code=end
