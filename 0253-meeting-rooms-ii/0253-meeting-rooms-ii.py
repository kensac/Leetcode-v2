class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []

        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        
        available = 0
        events.sort()
        for time, event in events:
            if event == 1:
                if available == 0:
                    available += 1
                if available != 0:
                    available -= 1
            elif event == -1:
                available += 1
        return available
                