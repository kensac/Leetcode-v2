class Solution:

    def __init__(self, w: list[int]):
        self.w = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.w.append(self.total)
            


    def pickIndex(self) -> int:
        random_number = random.randint(1, self.total)
        return bisect_left(self.w, random_number)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()