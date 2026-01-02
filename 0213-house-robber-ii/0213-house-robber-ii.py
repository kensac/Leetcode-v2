class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def robber(houses):
            prev_one = 0
            prev_two = 0
            for val in houses:
                prev_one, prev_two = max(prev_one, prev_two + val), prev_one
            return prev_one

        return max(robber(nums[1:].copy()), robber(nums[:-1]))
