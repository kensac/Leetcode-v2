class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(speed):
            hours = 0
            for pile in piles:
                hours += (pile // speed) + (1 if (pile % speed) else 0)
            
            return hours <= h
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if can_eat(mid):
                right = mid
            else:
                left = mid + 1
        
        return right
