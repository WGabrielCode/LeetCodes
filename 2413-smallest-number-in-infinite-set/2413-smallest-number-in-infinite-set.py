class SmallestInfiniteSet:
    def __init__(self):
        from queue import PriorityQueue
        self.curr = 1
        self.que = PriorityQueue()
        self.set = set()
    def popSmallest(self) -> int:
        if self.que.empty() :
            result = self.curr
            self.curr += 1
            return result 
        item = self.que.get()
        self.set.remove( item )
        return item
    def addBack(self, num: int) -> None:
        if num < self.curr and not (num in self.set) :
            self.que.put( num )
            self.set.add( num )