#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#


# @lc code=start
from typing import Dict


class Trie:
    # space complexity: O(N*S) S represents length of the word
    # time complexity: O(S)
    class Node:
        def __init__(self, path: str) -> None:
            self.path = path
            self.children: Dict[str, Trie.Node] = {}
            self.is_end = False

    def __init__(self):
        self.root = Trie.Node("")

    def insert(self, word: str) -> None:
        root_node = self.root

        for i in range(len(word)):
            c = word[i]

            if c not in root_node.children:
                root_node.children[c] = Trie.Node(c)
            root_node = root_node.children[c]
        root_node.is_end = True

    def search(self, word: str) -> bool:
        root_node = self.root

        for i in range(len(word)):
            c = word[i]
            if c not in root_node.children:
                return False

            root_node = root_node.children[c]

        return root_node.is_end

    def startsWith(self, prefix: str) -> bool:
        root_node = self.root

        for i in range(len(prefix)):
            c = prefix[i]
            if c not in root_node.children:
                return False

            root_node = root_node.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
