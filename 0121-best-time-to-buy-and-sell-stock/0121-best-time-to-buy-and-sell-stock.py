class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        res = 0
        for val in prices:
            min_price = min(min_price, val)
            res = max(val - min_price, res)

        return res
