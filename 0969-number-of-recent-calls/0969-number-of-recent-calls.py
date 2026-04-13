from collections import deque 
class RecentCounter:

    def __init__(self):
        self.que = deque()
        self.size = 0 

    def ping(self, t: int) -> int:
        min_t = t - 3000
        q = self.que
        while self.que and q[0] < min_t:
            self.size -= 1
            q.popleft()
        q.append(t)
        self.size += 1
        return self.size
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)