class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        l = r = 0

        while l <= r and r < len(nums):
            print(l, nums[l], r, nums[r], k, res)
            if nums[r] == 0:
                k -= 1
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            res = max((r - l) + 1, res)
            r += 1
        return res
