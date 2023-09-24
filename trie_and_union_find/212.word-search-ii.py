#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
from typing import Dict, List, Optional


class Solution:
    class Trie:
        class Node:
            def __init__(self) -> None:
                self.children: Dict[str, Solution.Trie.Node] = {}
                self.is_end = False
                self.word = ""

        def __init__(self) -> None:
            self.root = Solution.Trie.Node()

        def insert(self, word: str):
            root = self.root
            for c in word:
                if c not in root.children:
                    root.children[c] = Solution.Trie.Node()
                root = root.children[c]
            root.word = word
            root.is_end = True

        def is_prefix(self, word: str) -> Optional[Node]:
            root = self.root
            for c in word:
                if c not in root.children:
                    return None
                root = root.children[c]
            return root

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trie and Backtracking
        # time complexity: O(M*N*logL) L represents lenght of word
        # space complexity: O(K*L) k=len(words) L=Max length of word

        trie = Solution.Trie()

        for word in words:
            trie.insert(word)

        def backtrack(dx: int, dy: int, root: Solution.Trie.Node):
            ch = board[dx][dy]
            node = root.children[ch]
            if node.is_end:
                out.add(node.word)

            if not node.children:
                root.children.pop(ch)
                return

            board[dx][dy] = "#"
            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = dx + direction[0], dy + direction[1]
                if 0 <= x < m and 0 <= y < n and board[x][y] in node.children:
                    backtrack(x, y, node)
            board[dx][dy] = ch

        out = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    backtrack(i, j, trie.root)
        return list(out)


# @lc code=end
