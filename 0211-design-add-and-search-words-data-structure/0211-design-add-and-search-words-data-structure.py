class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        cur = self.trie
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur["*"] = {}

    def search(self, word: str) -> bool:
        # Recursively check for word if . else regular
        def recurse(trie, word):
            for i, char in enumerate(word):
                if char == ".":
                    return any(
                        [
                            recurse(lower_trie, word[i + 1 :])
                            for lower_trie in trie.values()
                        ]
                    )
                if char not in trie:
                    return False
                trie = trie[char]

            return "*" in trie

        return recurse(self.trie, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
