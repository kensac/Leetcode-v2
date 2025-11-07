class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0

        def in_bounds(i, j):
            if i < 0 or i >= len(grid):
                return False
            if j < 0 or j >= len(grid[0]):
                return False
            return True

        def dfs(x, y):
            grid[x][y] = 0
            cur = 1
            for dx, dy in DELTA:
                new_x, new_y = x + dx, y + dy
                if in_bounds(new_x, new_y) and grid[new_x][new_y] == 1:
                    cur += dfs(new_x, new_y)
            return cur

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(dfs(i, j), res)

        return res
