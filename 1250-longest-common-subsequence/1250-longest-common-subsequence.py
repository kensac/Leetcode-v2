class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for _ in range(len(text1))] for _ in range(len(text2))]

        for i in range(len(text2)):
            for j in range(len(text1)):
                if text1[j] == text2[i]:
                    grid[i][j] = (grid[i - 1][j - 1] if i > 0 and j > 0 else 0) + 1
                else:
                    top = grid[i - 1][j] if i > 0 else 0
                    left = grid[i][j - 1] if j > 0 else 0
                    grid[i][j] = max(top, left)
        return grid[-1][-1]