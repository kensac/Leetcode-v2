class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""

        word1_tracker = 0
        word2_tracker = 0

        while word1_tracker < len(word1) and word2_tracker < len(word2):
            res += word1[word1_tracker]
            res += word2[word2_tracker]

            word1_tracker += 1
            word2_tracker += 1

        res += word1[word1_tracker:] or word2[word2_tracker:]

        return res
