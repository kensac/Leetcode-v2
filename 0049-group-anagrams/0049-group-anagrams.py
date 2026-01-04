class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        How would you solve with unicode, sort the anagram map that costs more time but would support any amount or types of chars
        """
        anagram_map = defaultdict(list)
        for word in strs:
            counter = [0 for _ in range(26)]
            for char in word:
                counter[ord(char) - ord('a')] += 1
            anagram_map[tuple(counter)].append(word)
        
        return list(anagram_map.values())
