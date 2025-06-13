class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}"}
        stack = []
        for char in s:
            if char in d:
                stack.append(char)
            else:
                if (not stack) or (char != d[stack.pop()]):
                    return False

        return not stack
