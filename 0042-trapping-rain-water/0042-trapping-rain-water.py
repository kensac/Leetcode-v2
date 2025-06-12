class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        for i in range(1, len(left_max)):
            left_max[i] = max(left_max[i - 1], height[i - 1])
        right_max = [0] * len(height)
        for i in range(len(right_max) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i + 1])
        
        res = 0
        for i in range(len(height)):
            to_add = min(left_max[i], right_max[i]) - height[i]
            if to_add > 0:
                res += to_add
        return res