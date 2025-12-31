class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        self.results = []
        self._backtrack(s, word_set, [], 0)
        return self.results

    def _backtrack(self, s, word_set, current_sentence, start_idx):
        if start_idx == len(s):
            self.results.append(" ".join(current_sentence))
        
        for end_index in range(start_idx + 1, len(s) + 1):
            word = s[start_idx: end_index]

            if word in word_set:
                current_sentence.append(word)
                self._backtrack(s, word_set, current_sentence, end_index)
                current_sentence.pop()
