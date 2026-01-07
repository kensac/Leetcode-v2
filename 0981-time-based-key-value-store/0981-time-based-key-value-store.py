class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        entries = self.map[key]

        """
        # Find first larger than timestamp

        L     M     R
        F F F T T T T
        0 1 2 3 4 5 6
        """
        left = 0
        right = len(entries)
        while left < right:
            mid = (left + right) // 2
            if entries[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        self.map[key].insert(left, (timestamp, value))
        #print(self.map)


    def get(self, key: str, timestamp: int) -> str:
        """
        get number smaller than or equal to timestamp
        L     M     R
        T T T T F F F
        0 1 2 3 4 5 6
        """
        entries = self.map[key]
        if not entries or timestamp < entries[0][0]:
            return ""
        left = 0
        right = len(entries)
        while left < right:
            mid = (left + right) // 2
            if entries[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return entries[left - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)