class BrowserHistory:

    def __init__(self, homepage: str):
        self.queue = [homepage]
        self.cur = 0

    def visit(self, url: str) -> None:
        self.queue = self.queue[:self.cur + 1]
        self.queue.append(url)
        self.cur += 1

    def back(self, steps: int) -> str:
        self.cur -= steps
        self.cur = max(self.cur, 0)
        
        return self.queue[self.cur]

    def forward(self, steps: int) -> str:
        self.cur += steps
        self.cur = min(self.cur, len(self.queue) - 1)

        return self.queue[self.cur]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)