class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = defaultdict(int)

        for char in s:
            counter[char] += 1
        
        for char in t:
            counter[char] -= 1
        
        return all(i == 0 for i in counter.values())