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

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # BFS solution
        # time complexity: O(N*L) N=len(start) L=len(bank)
        # space complexity: O(L)

        from collections import deque

        q = deque()
        q.append((start, 0))
        bankSet = set(bank)

        while q:
            gene, step = q.popleft()
            if gene == end:
                return step

            for i, _ in enumerate(gene):
                for x in "ACGT":
                    mutation = gene[:i]+x+gene[i+1:]
                    if mutation != gene and mutation in bankSet:
                        bankSet.remove(mutation)
                        q.append((mutation, step+1))

        return -1
# @lc code=end
