class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, j, idx):
            if idx == len(word):
                return True
            if not (0 <= i < len(board)):
                return False
            
            if not (0 <= j < len(board[0])):
                return False

            if board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = "#"

            if (
                backtrack(i + 1, j, idx + 1)
                or backtrack(i, j + 1, idx + 1)
                or backtrack(i - 1, j, idx + 1)
                or backtrack(i, j - 1, idx + 1)
            ):
                return True

            board[i][j] = temp

        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0):
                    return True
        return False
