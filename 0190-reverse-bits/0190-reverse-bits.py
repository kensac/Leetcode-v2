class Solution:
    def reverseBits(self, n: int) -> int:
        rev = 0
        power = 31
        while n:
            bit = n & 1
            n >>= 1
            # the idea is to place this directly how many space behind we need
            rev += bit << power
            power -= 1
        return rev
