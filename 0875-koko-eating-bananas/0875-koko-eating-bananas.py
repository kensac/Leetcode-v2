class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(piles, k, h):
            hours = 0
            for pile in piles:
                hours += (pile // k) + (1 if pile % k else 0)
            return hours <= h

        left = 1
        right = max(piles)

        """
              L M    R
        F F F F T T T
        0 1 2 3 4 5 6
        """
        while left < right:
            mid = (left + right) // 2
            if can_eat(piles, mid, h):
                right = mid
            else:
                left = mid + 1

        return left
