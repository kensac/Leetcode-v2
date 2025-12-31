class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        # dp[i] will store wether we can make the word till here from the words in word dict
        # we assume 0 because it is empty string and then word for evrry char forward
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
        
        return dp[-1]