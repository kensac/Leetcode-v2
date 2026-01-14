class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        number_of_meetings_in_room = [0 for _ in range(n)]
        active_meeting_heap = []
        available_rooms = [i for i in range(n)]
        meetings.sort()

        for start, end in meetings:
            while active_meeting_heap and active_meeting_heap[0][0] <= start:
                _, room = heappop(active_meeting_heap)
                heappush(available_rooms, room)
            if available_rooms:
                room = heappop(available_rooms)
                heappush(active_meeting_heap, (end, room))
            else:
                old_end, room = heappop(active_meeting_heap)
                heappush(active_meeting_heap, (old_end + end - start, room))
            number_of_meetings_in_room[room] += 1

        return number_of_meetings_in_room.index(max(number_of_meetings_in_room))
