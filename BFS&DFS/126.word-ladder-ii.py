#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] Word Ladder II
#

# @lc code=start

from typing import List


class Node:
    def __init__(self, val: str) -> None:
        self.val = val
        self.pre = None


class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     # BFS: correct but (TLE)
    #     # time complexity: O(N*C*26) N=len(wordList) C=len(word)
    #     # space complexity: O(N*C)

    #     if endWord not in wordList:
    #         return []

    #     visited = set([beginWord])

    #     result = []
    #     q = [(beginWord, [beginWord])]

    #     while q:
    #         newVisited = set()
    #         nq = []
    #         for item in q:
    #             word, step = item
    #             for i, _ in enumerate(word):
    #                 for c in range(26):
    #                     nw = word[:i]+chr(ord('a')+c)+word[i+1:]
    #                     if nw in wordList and nw not in visited:
    #                         if nw == endWord:
    #                             result.append(step+[nw])
    #                         nq.append((nw, step+[nw]))
    #                         newVisited.add(nw)

    #         if result:
    #             return result
    #         visited |= newVisited
    #         q = nq

    #     return result

    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     # BFS: using linked list to store steps.(TLE)
    #     # time complexity: O(N*C*26) N=len(wordList) C=len(word)
    #     # space complexity: O(N*C)

    #     visited = set()
    #     visited.add(beginWord)

    #     q = [(beginWord, Node(beginWord))]

    #     def dfs(node: Node):
    #         tmp = []
    #         while node:
    #             tmp.append(node.val)
    #             node = node.pre
    #         res.append(tmp[::-1])

    #     res = []

    #     while q:
    #         nv = set()
    #         nq = []
    #         for item in q:
    #             word, node = item
    #             for i, _ in enumerate(word):
    #                 for c in range(26):
    #                     nw = word[:i]+chr(ord('a')+c)+word[i+1:]
    #                     if nw in wordList and nw not in visited:
    #                         nn = Node(nw)
    #                         nn.pre = node
    #                         if nw == endWord:
    #                             dfs(nn)
    #                         nq.append((nw, nn))
    #                         nv.add(nw)
    #         visited |= nv
    #         q = nq

    #     return res

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # BFS: BFE with backtracking
        # time complexity: O(C*N^2) N=len(wordList) C=len(word)
        # space complexity: O(N)
        '''
        best explanation: https://leetcode.com/problems/word-ladder-ii/discuss/2424910/Explanation-with-Animation

        1.Don't use bfs only and compute the paths during bfs. Instead,
        only use bfs to find the length of the shortest path, and then
        use dfs to output the shortest paths. Otherwise you may encounter
        exponentially many "potential" shortest paths, but only one of them
        is the real solution.Bidirectional-bfs codes fail for similar reasons.
        2.When using dfs to output the shortest paths, start from endWord instead
        of beginWord. Otherwise the running time can easily become exponential.
        This is because there are exponentially many dfs branches, but only one
        branch can give you the shortest path.Usually people perform bfs starting
        from beginWord. Then for each intermediate string, you know the shortest
        distance from it to beginWord, but don't know the shortest distance from
        it to endWord. If we perform dfs from endWord, we can discard those partial
        paths that cannot be extended into a shortest path, judging from the shortest
        distance from the current node to beginWord.
        (Starting dfs from beginWord could also work, but you need to carefully avoid those partial paths that cannot be extended into a shortest path.)
        '''

        from collections import deque

        def connected(a: str, b: str) -> bool:
            k = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    k += 1
            return k == 1

        if endWord not in wordList:
            return []

        visited = set([beginWord])

        q = deque([beginWord])
        nodes = []
        find = False

        # moving forward
        while q and not find:
            nodes.append(q.copy())
            n = len(q)
            for _ in range(n):
                word = q.popleft()

                for item in wordList:
                    if item in visited:
                        continue

                    if not connected(word, item):
                        continue

                    if item == endWord:
                        find = True
                        break

                    visited.add(item)
                    q.append(item)

                if find:
                    break

        if not find:
            return []

        ans = []

        def backtracking(word, level: int, steps: List[str]):
            if word == beginWord:
                ans.append(steps[::-1])
                return

            if level < 0:
                return

            for item in nodes[level]:
                if connected(item, word):
                    steps.append(item)
                    backtracking(item, level-1, steps)
                    steps.pop()

        # move backward to construct paths
        backtracking(endWord, len(nodes)-1, [endWord])

        return ans


# @lc code=end
