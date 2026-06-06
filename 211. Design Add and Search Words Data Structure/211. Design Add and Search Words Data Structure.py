#
# Problem: 211. Design Add and Search Words Data Structure
# Difficulty: Medium
# Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
# Language: python3
# Date: 2026-06-06


class TrieNode:
    __slots__ = ("children", "is_end")
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        return self._dfs(self.root, word, 0)
        
    def _dfs(self, node: TrieNode, word: str, i: int) -> bool:
        if i == len(word):
            return node.is_end

        ch = word[i]
        if ch == '.':
            for child in node.children.values():
                if self._dfs(child, word, i+1):
                    return True
            return False
        else:
            if ch not in node.children:
                return False
            return self._dfs(node.children[ch], word, i+1)
                
        


# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()

obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")

print(obj.search("a"))
print(obj.search(".at"))

obj.addWord("bat")
print(obj.search(".at"))

print(obj.search("an."))
print(obj.search("a.d."))

print(obj.search("b."))
print(obj.search("a.d."))

print(obj.search("."))
