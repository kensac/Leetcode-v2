class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False for _ in range(len(nums))]
        dp[0] = True
        for i, num in enumerate(nums):
            if not dp[i]:
                continue
            for i_add in range(num + 1):
                idx = min(i + i_add, len(nums) - 1)
                dp[idx] = True
            if dp[-1] == True:
                break
        
        return dp[-1]