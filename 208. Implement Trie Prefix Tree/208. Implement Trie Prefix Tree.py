#
# Problem: 208. Implement Trie (Prefix Tree)
# Difficulty: Medium
# Link: https://leetcode.com/problems/implement-trie-prefix-tree/description/
# Language: python3
# Date: 2026-06-06


class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children : dict[str, "TrieNode"] = {}
        self.is_end : bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find(prefix)
        return node is not None and node.is_end
        

    def startsWith(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, prefix: str) -> "TrieNode | None":
        trie = self.root
        for ch in prefix:
            if ch not in trie.children:
                return None
            trie = trie.children[ch]
        return trie
        


#Your Trie object will be instantiated and called as such:
word = "apple"
prefix = "app"
obj = Trie()
obj.insert(word)
param_2 = obj.search(word)
param_3 = obj.startsWith(prefix)
