class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search the row
        top, bottom = 0, len(matrix)
        """
        [
            T[1,3,5,7],
            [10,11,16,20],
            B[23,30,34,60]]
        """

        while top < bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target:
                top = mid + 1
            else:
                bottom = mid
        # invalid zone in [bottom to n]
        print(bottom, top)

        left, right = 0, len(matrix[0]) - 1

        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            print(mid)
            if matrix[top - 1][mid] == target:
                return True
            elif matrix[top - 1][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
            print(left, right)
        return False