class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(cur=[], left=0, right=0):
            #print(cur, left, right)
            if left == n and right == n:
                res.append("".join(cur))
                return
            
            if left < n:
                cur.append("(")
                backtrack(cur, left + 1, right)
                cur.pop()

            if right < left:
                cur.append(")")
                backtrack(cur, left, right + 1)
                cur.pop()

        backtrack()
        return res
