class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        [10]
        [2,2,1,0]
        res = [0] * len(heights)
        stack = []
        for i, height in enumerate(heights):
            while stack and stack[-1][1] < height:
                i_prev, _ = stack.pop()
                res[i_prev] += 1
            if stack:
                res[stack[-1][0]] += 1
            stack.append((i, height))
        return res
