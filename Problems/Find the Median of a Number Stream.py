from heapq import *


class MedianOfAStream:

    maxHeap = []
    minHeap = []

    def insert_num(self, num):
        if not self.maxHeap or -num >= self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap)) 

    def find_median(self):
        print(self.maxHeap)
        print(self.minHeap)
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return float(-self.maxHeap[0])


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(7)
    medianOfAStream.insert_num(9)
    medianOfAStream.insert_num(12)
    medianOfAStream.insert_num(15)
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(65)
    medianOfAStream.insert_num(42)
    print("The median is: " + str(medianOfAStream.find_median()))



main()
