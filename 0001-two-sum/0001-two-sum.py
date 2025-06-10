class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_find_index_map = {}

        for index, num in enumerate(nums):
            if num in to_find_index_map:
                return [to_find_index_map[num], index]
            else:
                to_find_index_map[target - num] = index
