from heapq import heappush, heappop
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        maxheap = []
        s = ''
        
        for char in s:
            if char not in d:
                d[char] = 0
            d[char] += 1
            
        for key in d:
            heappush(maxheap, (-d[key], key))
            
        while maxheap:
            entry = heappop(maxheap)
            s += (-entry[0] * entry[1])
            
        return s

print(Solution().frequencySort("tree"))