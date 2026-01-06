class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            count = 0
            while n:
                count += n & 1
                n >>= 1
            return count
        
        return [hammingWeight(i) for i in range(n + 1)]
        