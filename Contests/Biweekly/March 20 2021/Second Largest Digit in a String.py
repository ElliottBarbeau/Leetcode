from heapq import heappush, heappop
class Solution:
    def secondHighest(self, s: str) -> int:
        maxheap = []
        d = {}
        for char in s:
            if char.isdigit():
                if char not in d:
                    d[char] = 1
                    heappush(maxheap, -int(char))
        
        if not maxheap or len(maxheap) == 1:
            return -1
        heappop(maxheap)
        return -maxheap[0]