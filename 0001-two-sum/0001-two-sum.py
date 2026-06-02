class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_map = {}

        for i, num in enumerate(nums):
            if num in num_index_map:
                return [i, num_index_map[num]]
            num_index_map[target - num] = i
        