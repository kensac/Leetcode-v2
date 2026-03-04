class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        row_count = [0] * n
        col_count = [0] * m

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    row_count[i] += 1
                    col_count[j] += 1
        
        # Only neeed to check the row/col count at the points that have mat == 1 otherwise we would check positions that arent 1
        result = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and row_count[i] == 1 and col_count[j] == 1:
                    result += 1
        

        return result
