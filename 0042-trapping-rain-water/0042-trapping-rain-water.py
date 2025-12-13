class Solution:
    def trap(self, height: List[int]) -> int:
        """
        [1,0,2]
        left_map = [0,1,1]
        right_map = [2,2,0]
        """
        left_map = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            left_map[i] = max(left_map[i - 1], height[i - 1])

        right_map = [0 for _ in range(len(height))]
        for i in range(len(height) - 2, -1, -1):
            right_map[i] = max(right_map[i + 1], height[i + 1])

        water = 0

        for i in range(len(height)):
            
            water += max(0, min(left_map[i], right_map[i]) - height[i])

        return water
