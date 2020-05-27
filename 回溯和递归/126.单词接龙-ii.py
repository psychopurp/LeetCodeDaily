#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start


class Solution:
    # def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    #     import collections
    #     wordList = set(wordList)
    #     if endWord not in wordList:
    #         return []
    #     res = []
    #     layer = {}
    #     layer[beginWord] = [[beginWord]]
    #     visited = set()
    #     while layer:
    #         newlayer = collections.defaultdict(list)
    #         for w in layer:
    #             visited.add(w)
    #             if w == endWord:
    #                 res.extend(k for k in layer[w])
    #                 return res
    #             else:
    #                 neighbors = self.getNeighbor(w, wordList, visited)
    #                 for n in neighbors:
    #                     newlayer[n] += [j + [n] for j in layer[w]]
    #         layer = newlayer
    #     return res

    # def getNeighbor(self, word, wordSet, visited):
    #     res = []
    #     for i in range(len(word)):

    #         for j in "abcdefghijklmnopqrstuvwxyz":
    #             if j == word[i]:
    #                 continue
    #             tmp = word[:i] + j + word[i + 1:]
    #             if tmp not in visited and tmp in wordSet:
    #                 res.append(tmp)
    #     return res

    def findLadders(self, beginWord, endWord, wordList):
        import collections
        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww] += [j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res
# @lc code=end
