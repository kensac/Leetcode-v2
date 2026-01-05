class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for amount in range(len(dp)):
            for coin in coins:
                if amount - coin >= 0:
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)
                #print(dp)
        return dp[amount] if dp[amount] != float("inf") else -1