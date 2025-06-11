class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 0
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] = digits[i] + carry
            carry = digits[i] // 10
            digits[i] %= 10

        return [carry] + digits if carry else digits
