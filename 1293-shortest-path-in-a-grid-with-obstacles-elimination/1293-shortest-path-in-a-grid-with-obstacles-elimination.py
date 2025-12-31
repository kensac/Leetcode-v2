class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        target = (m - 1, n - 1)

        if k >= m + n - 2:
            return m + n - 2

        state = (0, 0, k)
        queue = Deque([(0, state)])
        seen = set([state])

        while queue:
            steps, (row, col, k) = queue.popleft()

            if (row, col) == target:
                return steps

            for new_row, new_col in [
                (row, col + 1),
                (row, col - 1),
                (row + 1, col),
                (row - 1, col),
            ]:
                if (0 <= new_row < m) and (0 <= new_col < n):
                    new_k = k - grid[new_row][new_col]
                    new_state = (new_row, new_col, new_k)
                    if new_k >= 0 and new_state not in seen:
                        seen.add(new_state)
                        queue.append((steps + 1, new_state))

        return -1
