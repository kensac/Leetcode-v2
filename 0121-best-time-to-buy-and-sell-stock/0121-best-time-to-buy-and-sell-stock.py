class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        profit = 0

        while l <= r and r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r += 1

        return profit
