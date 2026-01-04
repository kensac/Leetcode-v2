class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = "0"

            for new_x, new_y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if (
                    0 <= new_x < len(grid)
                    and 0 <= new_y < len(grid[0])
                    and grid[new_x][new_y] == "1"
                ):
                    dfs(new_x, new_y)

        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1

        return result
