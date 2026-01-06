class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()
        max_rooms = 0
        cur = 0
        for time, event in events:
            cur += event
            max_rooms = max(max_rooms, cur)
        
        return max_rooms