class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_oranges = []
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        if not fresh:
            return 0
        
        time = -1
        rotten_oranges = deque(rotten_oranges)
        while rotten_oranges:
            newly_rotten = []
            time += 1
            for x, y in rotten_oranges:
                for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if not 0 <= new_x < len(grid):
                        continue
                    if not 0 <= new_y < len(grid[0]):
                        continue
                    if grid[new_x][new_y] != 1:
                        continue
                    grid[new_x][new_y] = 2
                    newly_rotten.append((new_x, new_y))
                grid[x][y] = 0

            if newly_rotten:
                rotten_oranges = newly_rotten
            else:
                rotten_oranges = []
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time
