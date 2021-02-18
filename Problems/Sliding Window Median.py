import heapq
from heapq import heappop, heappush, heappushpop

class SlidingWindowMedian:
    minHeap, maxHeap = [], []
    def add_number(self, num):
        if not self.maxHeap:
            heappush(self.maxHeap, -num)
            return

        if num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        self.rebalance()

    def get_median(self):
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        return float(-self.maxHeap[0])

    def remove_number(self, num, heap):
        ind = heap.index(num)
        heap[ind] = heap[-1]
        del heap[-1]

        if ind < len(heap):
            heapq._siftup(heap, ind)
            heapq._siftdown(heap, 0, ind)

        self.rebalance()

    def rebalance(self):
        if len(self.maxHeap) - len(self.minHeap) > 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def find_sliding_window_median(self, nums, k):
        self.maxHeap, self.minHeap = [], []
        result = []
        window_start, window_end = 0, 0

        while window_end + 1 < k:
                self.add_number(nums[window_end])
                window_end += 1

        while window_end < len(nums):
            self.add_number(nums[window_end])

            if window_end - window_start >= k:
                elementToBeRemoved = nums[window_start]
                if elementToBeRemoved <= -self.maxHeap[0]:
                    self.remove_number(-elementToBeRemoved, self.maxHeap)
                else:
                    self.remove_number(elementToBeRemoved, self.minHeap)
                window_start += 1

            result.append(self.get_median())
            window_end += 1

        return result


def main():

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
