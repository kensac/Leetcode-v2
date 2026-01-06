class MedianFinder:
    from heapq import heappush_max, heappop_max

    def __init__(self):
        self.lower_max = []
        self.upper_min = []

    def addNum(self, num: int) -> None:
        heappush_max(self.lower_max, num)
        if self.upper_min and self.lower_max[0] > self.upper_min[0]:
            temp = heappop_max(self.lower_max)
            heappush(self.upper_min, temp)

        if len(self.lower_max) - len(self.upper_min) > 1:
            temp = heappop_max(self.lower_max)
            heappush(self.upper_min, temp)
        
        if len(self.upper_min) - len(self.lower_max) > 0:
            temp = heappop(self.upper_min)
            heappush_max(self.lower_max, temp)
        
        #print(self.lower_max, self.upper_min)

    def findMedian(self) -> float:
        if not self.lower_max:
            return float("inf")
        if len(self.lower_max) > len(self.upper_min):
            return self.lower_max[0]
        else:
            return (self.lower_max[0] + self.upper_min[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()