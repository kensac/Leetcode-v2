class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        start = cur = 0
        res = []
        while cur < len(nums):
            if nums[cur] + 1 in nums:
                cur += 1
                continue
            elif start == cur:
                res.append(f"{nums[cur]}")
                cur += 1
                start = cur
            else:
                res.append(f"{nums[start]}->{nums[cur]}")
                cur += 1
                start = cur
        return res