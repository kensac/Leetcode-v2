class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        # 26, rem = 0 columnNumber = 1
        # 28, rem = 2 columnNumber = 1 # B
        # 1, rem = 1 columnNumber = 0 # A
        while columnNumber:
            columnNumber -= 1
            remainder = columnNumber % 26
            columnNumber = columnNumber // 26
            res = chr(ord("A") + remainder) + res
        return res