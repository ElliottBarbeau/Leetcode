from heapq import *
class Solution:
    def solve(self, orders):
        buyheap = []
        sellheap = []
        for order in orders:
            if order[2] == 0:
                heappush(buyheap, (-order[0], order))
            else:
                heappush(sellheap, order)

        count = 0
        while buyheap and sellheap:
            curr_buy = heappop(buyheap)[1]
            while curr_buy[1] > 0 and sellheap:
                if curr_buy[0] >= sellheap[0][0] and sellheap[0][1] > 0:
                    if curr_buy[1] >= sellheap[0][1]:
                        count += sellheap[0][1]
                        curr_buy[1] -= sellheap[0][1]
                        sellheap[0][1] -= sellheap[0][1]
                    else:
                        count += curr_buy[1]
                        sellheap[0][1] -= curr_buy[1]
                        curr_buy[1] -= curr_buy[1]
                elif curr_buy[0] < sellheap[0][0]:
                    break
                else:
                    heappop(sellheap)

        return count

orders = [
    [150, 5, 0],
    [190, 1, 1],
    [200, 1, 1],
    [100, 9, 0],
    [140, 8, 1],
    [210, 4, 0]
]

print(Solution().solve(orders))

orders = [
    [1, 1, 0],
    [1, 4, 1],
    [2, 4, 0]
]

print(Solution().solve(orders))

orders = [
    [4, 2, 1],
    [1, 4, 1],
    [5, 4, 0],
    [2, 5, 0]
]

print(Solution().solve(orders))