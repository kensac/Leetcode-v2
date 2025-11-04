class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        heap = []
        max_heap_size = 0

        for start, end in intervals:
            while heap and start >= heap[0]:
                heappop(heap)
            
            heappush(heap, end)
            max_heap_size = max(max_heap_size, len(heap))
        
        return max_heap_size