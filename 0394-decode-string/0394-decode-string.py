class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                string_to_mul = []
                while stack and stack[-1] != "[":
                    string_to_mul = [stack.pop()] + string_to_mul
                # Popping the "["
                stack.pop()
                # deal with the numbers
                num_to_mul = ""
                while stack and stack[-1].isdigit():
                    num_to_mul = stack.pop() + num_to_mul

                string_to_mul = string_to_mul * int(num_to_mul)

                stack.extend(string_to_mul)

        return "".join(stack)