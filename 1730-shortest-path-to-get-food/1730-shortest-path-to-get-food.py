class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "*":
                    start_point = (i, j)

        queue = Deque([[start_point]])
        distance = 0
        seen = set((i, j))

        while queue:
            cur_level = queue.popleft()
            new_level = []
            for x, y in cur_level:
                if grid[x][y] == "#":
                    return distance
                for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (
                        0 <= new_x < len(grid)
                        and 0 <= new_y < len(grid[0])
                        and (new_x, new_y) not in seen
                        and grid[new_x][new_y] != "X"
                    ):
                        new_level.append((new_x, new_y))
                        seen.add((new_x, new_y))
            if new_level:
                queue.append(new_level)
                distance += 1

        return -1
