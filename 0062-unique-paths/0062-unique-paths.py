class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top = grid[i - 1][j] if i > 0 else 0
                left = grid[i][j - 1] if j > 0 else 0
                grid[i][j] = top + left
        #print(grid)
        return grid[m - 1][n - 1]
