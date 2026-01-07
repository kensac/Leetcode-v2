class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        edges = deque([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (
                    i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1
                ):
                    board[i][j] = "E"
                    edges.append((i, j))

        while edges:
            x, y = edges.popleft()

            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if not 0 <= new_x < len(board):
                    continue

                if not 0 <= new_y < len(board[0]):
                    continue

                if board[new_x][new_y] != "O":
                    continue

                board[new_x][new_y] = "E"
                edges.append((new_x, new_y))

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "E":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
