from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.total_len = 0
        

    def addNum(self, num: int) -> None:
        self.total_len += 1
        if not self.minheap or num >= self.minheap[0]:
            heappush(self.minheap, num)
        else:
            heappush(self.maxheap, -num)
            
        if len(self.minheap) - len(self.maxheap) >= 2:
            n = heappop(self.minheap)
            heappush(self.maxheap, -n)
        elif len(self.maxheap) - len(self.minheap) >= 1:
            n = -heappop(self.maxheap)
            heappush(self.minheap, n)
        

    def findMedian(self) -> float:
        if self.total_len % 2 == 0:
            return (-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return self.minheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()