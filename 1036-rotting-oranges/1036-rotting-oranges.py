class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def in_bounds(i, j):
            if i < 0 or i >= len(grid):
                return False
            if j < 0 or j >= len(grid[0]):
                return False
            return True

        # precompute t = 0
        cur_rotten = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    cur_rotten.append((i, j))

        t = 0
        queue = Deque([cur_rotten])
        while queue:
            cur_level = queue.popleft()
            new_level = []
            for x, y in cur_level:
                grid[x][y] = 0
                for dx, dy in DELTA:
                    new_x, new_y = x + dx, y + dy
                    if in_bounds(new_x, new_y) and grid[new_x][new_y] == 1:
                        grid[new_x][new_y] = 2
                        new_level.append((new_x, new_y))
            if new_level:
                t += 1
                queue.append(new_level)
        any_fresh = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    any_fresh = True

        return -1 if any_fresh else t
