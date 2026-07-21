class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord(char) - ord('a')] += 1
            groups[tuple(counter)].append(word)
        
        return list(groups.values())