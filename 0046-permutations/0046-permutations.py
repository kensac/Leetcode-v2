class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
            
            for num in nums:
                if num not in cur:
                    backtrack(cur + [num])
        backtrack([])
        return res