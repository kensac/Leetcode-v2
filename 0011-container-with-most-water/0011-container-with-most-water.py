class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            res = max((min(height[l], height[r]) * (r - l)), res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res
