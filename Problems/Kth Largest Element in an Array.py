from heapq import heappush, heappop, heappushpop
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        minheap = []
        for i in range(k):
            heappush(minheap, nums[i])
            
        for i in range(k, len(nums)):
            if nums[i] > minheap[0]:
                heappushpop(minheap, nums[i])
                
        return minheap[0]