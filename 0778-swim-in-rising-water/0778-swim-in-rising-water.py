class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        seen = set((0, 0))
        pq = [(grid[0][0], 0, 0)]
        ans = 0

        while pq:
            depth, row, col = heappop(pq)
            ans = max(ans, depth)

            if row == col == N - 1:
                return ans

            for new_row, new_col in [
                (row + 1, col),
                (row - 1, col),
                (row, col + 1),
                (row, col - 1),
            ]:
                if (
                    0 <= new_row < N
                    and 0 <= new_col < N
                    and (new_row, new_col) not in seen
                ):
                    heapq.heappush(pq, (grid[new_row][new_col], new_row, new_col))
                    seen.add((new_row, new_col))
