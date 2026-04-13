from collections import deque 
class RecentCounter:

    def __init__(self):
        self.que = deque()
    def ping(self, t: int) -> int:
        min_t = t - 3000
        q = self.que
        while q and q[0] < min_t:
            q.popleft()
        q.append(t)
        return len(q)
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)