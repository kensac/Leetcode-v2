class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        #print(self.events)
        i = 0

        # ignore any non overlapping intervals
        while i < len(self.events) and startTime >= self.events[i][1]:
            i += 1

        if i < len(self.events) and endTime > self.events[i][0]:
            return False

        self.events.insert(i, (startTime, endTime))

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
