class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(heights, initial_queue):
            queue = Deque(initial_queue)
            seen = set()

            while queue:
                x, y = queue.popleft()
                seen.add((x, y))

                for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if (
                        (0 <= new_x < len(heights))
                        and (0 <= new_y < len(heights[0]))
                        and (heights[x][y] <= heights[new_x][new_y])
                        and (new_x, new_y) not in seen
                    ):
                        queue.append((new_x, new_y))
            return seen

        pacific = []
        atlantic = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    pacific.append((i, j))
                if i == len(heights) - 1 or j == len(heights[0]) - 1:
                    atlantic.append((i, j))

        pacific_set = bfs(heights, pacific)
        atlantic_set = bfs(heights, atlantic)
        #print(pacific_set, atlantic_set)
        return [list(coord) for coord in pacific_set if coord in atlantic_set]
