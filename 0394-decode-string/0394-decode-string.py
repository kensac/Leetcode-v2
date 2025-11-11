class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        cur = 0
        while cur < len(s):
            print(stack)
            if s[cur] == "[":
                stack.append(s[cur])
                cur += 1
            elif s[cur].isalpha():
                stack.append(s[cur])
                cur += 1
            elif s[cur].isnumeric():
                temp = ""
                while s[cur].isnumeric():
                    temp += s[cur]
                    cur += 1
                stack.append(int(temp))
            elif s[cur] == "]":
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()  # "["
                num = stack.pop()
                stack.append(temp * num)
                cur += 1
        return "".join(stack)
