from heapq import heappop, heappush
class Solution:
    def getNumberOfBacklogOrders(self, orders: list[list[int]]) -> int:
        buyheap = []
        sellheap = []
        for order in orders:
            if order[2] == 0:
                while sellheap and sellheap[0][1][0] <= order[0]:
                    if order[1] >= sellheap[0][1][1]:
                        order[1] -= sellheap[0][1][1]
                        heappop(sellheap)
                    else:
                        sellheap[0][1][1] -= order[1]
                        order[1] = 0
                        break
                        
                if order[1] > 0:
                    heappush(buyheap, (-order[0], order))
            else:
                while buyheap and -buyheap[0][0] >= order[0]:
                    if order[1] >= buyheap[0][1][1]:
                        order[1] -= buyheap[0][1][1]
                        heappop(buyheap)
                    else:
                        buyheap[0][1][1] -= order[1]
                        order[1] = 0
                        break
                        
                if order[1] > 0:
                    heappush(sellheap, (order[0], order))
                    
        total = 0
        while sellheap:
            x, curr = heappop(sellheap)
            total += curr[1]
            print(x)
            
        while buyheap:
            x, curr = heappop(buyheap)
            total += curr[1]
            print(x)
            
        return total % (10**9 + 7)