#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#

# @lc code=start
from typing import List


class Solution:
    # def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    #     # BFS solution with preprocessing
    #     # time complexity: O(N*L) N=len(start) L=len(bank)
    #     # space complexity: O(L)
    #     from collections import deque

    #     q = deque()
    #     q.append((start, 0))
    #     visited = set()

    #     # preprocessing
    #     general_dict: Dict[str, List[str]] = {}
    #     for gene in bank:
    #         for i, _ in enumerate(gene):
    #             template = gene[:i] + "*" + gene[i+1:]
    #             general_dict.setdefault(template, [])
    #             general_dict[template].append(gene)

    #     while q:
    #         gene, step = q.popleft()
    #         if gene == end:
    #             return step

    #         visited.add(gene)
    #         for i, _ in enumerate(gene):
    #             template = gene[:i] + "*" + gene[i+1:]
    #             for item in general_dict.get(template, []):
    #                 if item not in visited:
    #                     q.append((item, step+1))

    #     return -1

    # def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    #     # BFS solution
    #     # time complexity: O(N*L) N=len(start) L=len(bank)
    #     # space complexity: O(L)

    #     from collections import deque

    #     q = deque()
    #     q.append((start, 0))
    #     bankSet = set(bank)

    #     while q:
    #         gene, step = q.popleft()
    #         if gene == end:
    #             return step

    #         for i, _ in enumerate(gene):
    #             for x in "ACGT":
    #                 mutation = gene[:i]+x+gene[i+1:]
    #                 if mutation != gene and mutation in bankSet:
    #                     bankSet.remove(mutation)
    #                     q.append((mutation, step+1))

    #     return -1

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # BFS: two-end bfs implementation with time improvement by can_change function
        # time complexity: O(N*C) N=len(bank) C=len(startGene)
        # space complexity: O(N*C)

        if endGene not in bank:
            return -1

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

        q_start, q_end = deque([startGene]), deque([endGene])
        visited_start, visited_end = set([startGene]), set([endGene])

        level = -1

        while q_start and q_end:
            # the crucial part of two-end BFS
            if len(q_end) < len(q_start):
                q_start, q_end = q_end, q_start
                visited_start, visited_end = visited_end, visited_start

            level += 1
            for _ in range(len(q_start)):
                word = q_start.popleft()
                if word in visited_end:
                    return level

                for next_word in bank:
                    if next_word not in visited_start and can_change(word, next_word):
                        visited_start.add(next_word)
                        q_start.append(next_word)

        return -1


# @lc code=end
