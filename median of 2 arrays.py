from heapq import *

class Solution:
    min_heap = []
    max_heap = []
    
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        total_len = len(nums1) + len(nums2)
        for num in nums1:
            self.insert(num)
            
        for num in nums2:
            self.insert(num)
            
        if total_len % 2 == 0:
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return float(self.min_heap[0])
        
    def insert(self, num):
        if not self.min_heap:
            heappush(self.min_heap, num)
        else:
            if num >= self.min_heap[0]:
                heappush(self.min_heap, num)
            else:
                heappush(self.max_heap, -num)
            if len(self.min_heap) - len(self.max_heap) >= 2:
                heappush(self.max_heap, -heappop(self.min_heap))
            elif len(self.max_heap) > len(self.min_heap):
                heappush(self.min_heap, -heappop(self.max_heap))
        
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))