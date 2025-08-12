class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEat(mid):
            t = 0
            for p in piles:
                t += ceil(p / mid)
            return t <= h

        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low) // 2
            if canEat(mid):
                high = mid
            else:
                low = mid + 1
        return low
