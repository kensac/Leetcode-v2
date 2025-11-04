class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}

        for i, num in enumerate(nums):
            if num in num_index_map:
                return [num_index_map[num], i]
            num_index_map[target - num] = i