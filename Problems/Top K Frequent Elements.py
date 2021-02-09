from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums, k: int):
        d = {}
        maxheap = []
        res = []
        
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
            
        for key in d:
            heappush(maxheap, (-d[key], key))
            
        while k > 0:
            res.append(heappop(maxheap)[1])
            k -= 1
            
        return res