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

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS: 4.two-end BFS imporved based on two-end solution 2
        # time complexity: O(N*C^2) N=len(wordList) C=len(word)
        # space complexity: O(N*C^2)

        from collections import deque

        if endWord not in wordList:
            return 0

        patterns: Dict[str, List[str]] = {}
        for word in wordList:
            for i, _ in enumerate(word):
                template = word[:i]+"*"+word[i+1:]
                patterns.setdefault(template, []).append(word)

        q1 = deque([(beginWord, 1)])
        q2 = deque([(endWord, 1)])

        visited1 = {beginWord: 1}
        visited2 = {endWord: 1}

        def update(word: str, step: int, q: deque, visited1: Dict[str, int], visited2: Dict[str, int]) -> int:
            for i, _ in enumerate(word):
                template = word[:i]+"*"+word[i+1:]
                for item in patterns.get(template, []):
                    if item in visited2:
                        return step+visited2[item]
                    if item not in visited1:
                        visited1[item] = step+1
                        q.append((item, step+1))
            return 0

        while q1 and q2:
            # search the shortest end first
            if len(q2) < len(q1):
                q1, q2 = q2, q1
                visited1, visited2 = visited2, visited1

            for _ in range(len(q1)):
                word, step = q1.popleft()
                ret = update(word, step, q1, visited1, visited2)
                if ret:
                    return ret

        return 0


# @lc code=end
