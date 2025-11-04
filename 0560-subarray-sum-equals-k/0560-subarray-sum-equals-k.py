class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        sum_map = {}
        sum_map[0] = 1

        for num in nums:
            cur_sum += num
            if cur_sum - k in sum_map:
                count += sum_map[cur_sum - k]
            sum_map[cur_sum] = sum_map.get(cur_sum, 0) + 1
        
        return count