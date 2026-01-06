class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Choose interval with shorter end when we have merge overlap
        stack = []
        intervals.sort()
        res = 0
        for start, end in intervals:
            if stack and stack[-1][1] > start:
                stack[-1][1] = min(end, stack[-1][1])
                res += 1
            else:
                stack.append([start, end])
        
        return res