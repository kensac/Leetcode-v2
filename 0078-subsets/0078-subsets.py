class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def backtrack(idx = 0, cur = []):
            if idx >=len(nums):
                self.res.append(cur[:])
                return
            
            backtrack(idx + 1, cur + [nums[idx]])
            backtrack(idx + 1, cur)
            
        backtrack(0, [])
        return self.res
