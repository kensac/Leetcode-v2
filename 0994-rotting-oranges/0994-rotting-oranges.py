class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY_CELL = 0
        FRESH_ORANGE = 1
        ROTTEN_ORANGE = 2

        DIRS = [(1,0), (0,1), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])

        queue = deque([])
        fresh_oranges = 0 # 6

        first_rotten_oranges = [] # [(0, 0)]
        for i in range(n):
            for j in range(m):
                orange = grid[i][j]
                if orange == FRESH_ORANGE:
                    fresh_oranges += 1
                elif orange == ROTTEN_ORANGE:
                    first_rotten_oranges.append((i, j))

        if first_rotten_oranges:
            queue.append(first_rotten_oranges)
        
        if fresh_oranges == 0:
            return 0
        
        time = 0
        
        while queue: # [[(0, 0)]]
            # grid = [[0,1,1],[1,1,0],[0,1,1]]
            print(queue)
            cur_level = queue.popleft() # [(0, 0)]
            new_rotten_oranges = []
            for i, j in cur_level:
                grid[i][j] = EMPTY_CELL
                for dx, dy in DIRS:
                    new_x, new_y = i + dx, j + dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == FRESH_ORANGE:
                        grid[new_x][new_y] = ROTTEN_ORANGE
                        fresh_oranges -= 1
                        new_rotten_oranges.append((new_x, new_y))
            
            if new_rotten_oranges:
                queue.append(new_rotten_oranges)
                time += 1
        print(fresh_oranges, time)
        
        return time if not fresh_oranges else -1