class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        N = len(nums)

        rob_next_plus_one = 0
        rob_next = nums[N - 1]

        for i in range(N - 2, -1, -1):
            current = max(nums[i] + rob_next_plus_one, rob_next)

            rob_next_plus_one = rob_next
            rob_next = current
        
        return rob_next