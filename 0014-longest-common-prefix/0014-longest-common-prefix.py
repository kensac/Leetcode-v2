class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        pref = ""

        for char in first_word:
            len_pref = len(pref)
            for word in strs:
                if len_pref == len(word):
                    return pref
                if word[len_pref : len_pref + 1] != char:
                    return pref
            pref += char

        return pref
