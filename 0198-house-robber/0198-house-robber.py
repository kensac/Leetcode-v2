class Solution:
    def rob(self, nums: List[int]) -> int:
        "prev_one need to be initialzied to the max value of 0 and 1 to handle skips"
        if len(nums) < 3:
            return max(nums)
        
        prev_two = nums[0]
        prev_one = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            prev_one, prev_two, =  max(prev_one, prev_two + nums[i]), prev_one
        
        return max(prev_one, prev_two)