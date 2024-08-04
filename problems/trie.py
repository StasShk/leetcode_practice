### https://leetcode.com/problems/implement-trie-prefix-tree


class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['*'] = ""

    def search(self, word: str) -> bool:
        cur = self.root
        last = word[-1]
        for w in word:
            if w in cur:
                cur = cur[w]
            else:
                return False
        return "*" in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w in cur:
                cur = cur[w]
            else:
                return False
        return True

