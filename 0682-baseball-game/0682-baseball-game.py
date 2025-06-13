class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = 0
        stack = []

        for char in operations:
            if char == "+":
                stack.append(stack[-1] + stack[-2])
            elif char == "D":
                stack.append(2 * stack[-1])
            elif char == "C":
                stack.pop()
            else:
                stack.append(int(char))

        return sum(stack)
