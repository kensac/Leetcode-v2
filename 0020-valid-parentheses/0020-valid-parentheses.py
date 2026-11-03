class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_pairs = {"(": ")", "[": "]", "{": "}"}

        for char in s:
            if char in paren_pairs:
                stack.append(char)
            elif stack and paren_pairs[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return not stack
