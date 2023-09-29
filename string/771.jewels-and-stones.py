#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] Jewels and Stones
#


# @lc code=start
class Solution:
    # def numJewelsInStones(self, jewels: str, stones: str) -> int:
    #     # Brute force
    #     # time complexity: O(M*N) M=len(stones) N=len(jewels)
    #     # space complexity: O(1)
    #     count = 0
    #     for s in stones:
    #         if s in jewels:
    #             count += 1
    #     return count

    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Hash
        # time complexity: O(M+N) M=len(stones) N=len(jewels)
        # space complexity: O(N)

        hash = {}
        for s in jewels:
            hash[s] = True

        count = 0
        for s in stones:
            if s in hash:
                count += 1
        return count


# @lc code=end
