class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        left_mul = 1
        for i in range(len(nums)):
            result[i] *= left_mul
            left_mul *= nums[i]

        right_mul = 1
        for i in range(len(nums) - 1, - 1, - 1):
            result[i] *= right_mul
            right_mul *= nums[i]
        
        return result