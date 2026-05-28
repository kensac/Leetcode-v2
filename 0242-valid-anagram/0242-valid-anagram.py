class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        for char in t:
            counter[char] = counter.get(char, 0) - 1
        
        return all(count == 0 for count in counter.values())