class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_volume = 0

        while l < r:
            max_volume = max(max_volume, (r - l) * min(height[r], height[l]))
            #print(height[r], height[l], r, l)
            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        
        return max_volume
