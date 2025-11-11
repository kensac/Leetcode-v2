class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        DIRECTION = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        cur_dir = 0
        i, j = 0, 0

        def is_valid(i, j):
            if i < 0 or i >= len(matrix):
                return False
            if j < 0 or j >= len(matrix[0]):
                return False
            if matrix[i][j] == "#":
                return False
            return True

        while len(res) != len(matrix) * len(matrix[0]):
            res.append(matrix[i][j])
            matrix[i][j] = "#"
            if not is_valid(i + DIRECTION[cur_dir][0], j + DIRECTION[cur_dir][1]):
                cur_dir += 1
                if cur_dir > 3:
                    cur_dir = 0
            i = i + DIRECTION[cur_dir][0]
            j = j + DIRECTION[cur_dir][1]

        return res
