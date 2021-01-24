from heapq import *

class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        total = 0
        maxHeap = []
        if truckSize == 0:
            return 0
        
        for box in boxTypes:
            heappush(maxHeap, (-box[1], box[0]))
        
        while maxHeap and truckSize > 0:
            range = 0
            while truckSize > 0 and range < maxHeap[0][1]:
                total += -maxHeap[0][0]
                range += 1
                truckSize -= 1
            
            heappop(maxHeap)
                
        return total

print(Solution().maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))