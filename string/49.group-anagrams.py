#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # time complexity: O(n*k)
        # space complexity: O(n*k)

        import collections

        def genKey(s: str) -> List[int]:
            counter = [0]*26
            for i in s:
                counter[ord(i)-ord('a')] += 1
            return counter

        hash = collections.defaultdict(list)

        for s in strs:
            counter = genKey(s)
            hash[tuple(counter)].append(s)

        return list(hash.values())


# @lc code=end
