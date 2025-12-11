class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        """
        [
        [1,0,1,0,0],
        [1,0,1,2,3],
        [1,2,3,4,5],
        [1,0,0,1,0]
        ]
        """
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i][j - 1] + 1, 1)
                
                    cur_max = dp[i][j]
                    for offset in range(i, -1, -1):
                        diff = i - offset
                        cur_max = min(dp[i - diff][j], cur_max)
                        res = max(res, cur_max * (diff + 1))
        return res
