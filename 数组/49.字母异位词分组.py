#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     # 时间复杂度O(NKlog K) N为strs长度 KlogK 为字符串排序时间
    #     # 空间复杂度 O(N)
    #     dic = {}
    #     for s in strs:
    #         dic[tuple(sorted(s))] = dic.get(tuple(sorted(s)), []) + [s]
    #     return list(dic.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 时间复杂度O(NK) N为strs长度 而 K 是 strs 中字符串的最大长度
        # 空间复杂度 O(N)
        dic = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            dic[tuple(count)] = dic.get(tuple(count), []) + [s]
        return list(dic.values())

# @lc code=end
