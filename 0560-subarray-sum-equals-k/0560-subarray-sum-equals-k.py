class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cur_sum = 0
        sum_map = {}
        sum_map[0] = 1

        # This is such a nice idea but we store the sum we encounter and the number of times we have seen it before
        # the idea is when we see cur_sum - k in the map everything between cur and that val equal k
        # we increment the count by the count in sum_map because that is how. many instances of the exact sum we have seen already before we got here
        # 1 -1 1 -1 1, k = 0 work this one out to understand count


        for num in nums:
            cur_sum += num
            if cur_sum - k in sum_map:
                count += sum_map[cur_sum - k]
            sum_map[cur_sum] = sum_map.get(cur_sum,0) + 1

        return count
