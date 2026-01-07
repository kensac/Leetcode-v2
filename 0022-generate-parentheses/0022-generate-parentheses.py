class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur, left, right):
            if right > left or left > n or right > n:
                return
            if left == n and left == right:
                res.append(cur[:])
                return
            backtrack(cur + '(', left + 1, right)
            backtrack(cur + ')', left, right + 1)


        backtrack("", 0, 0)
        return res