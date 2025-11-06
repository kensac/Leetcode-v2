class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [
            [0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))
        ]
        dp[0][0] = 1 if not obstacleGrid[0][0] else 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0:
                    continue
                top = dp[i - 1][j] if i > 0 else 0
                left = dp[i][j - 1] if j > 0 else 0
                dp[i][j] = top + left if not obstacleGrid[i][j] else 0

        return dp[-1][-1]
