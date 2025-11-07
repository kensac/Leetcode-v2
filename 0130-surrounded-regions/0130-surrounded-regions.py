class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(row, col):
            if board[row][col] != "O":
                return
            board[row][col] = "E"
            if col < COLS - 1:
                dfs(row, col + 1)
            if row < ROWS - 1:
                dfs(row + 1, col)
            if col > 0:
                dfs(row, col - 1)
            if row > 0:
                dfs(row - 1, col)

        border_cells = []

        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1:
                    border_cells.append((i, j))

        for i, j in border_cells:
            dfs(i, j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "E":
                    board[i][j] = "O"
