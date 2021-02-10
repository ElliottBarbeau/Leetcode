from heapq import heappush, heappop
class Solution:
    def kClosest(self, points, K):
        maxheap = []
        res = []
        for i in range(K):
            point = points[i]
            dist = point[0] ** 2 + point[1] ** 2
            heappush(maxheap, (-dist, [point[0], point[1]]))

        for i in range(K, len(points)):
            point = points[i]
            dist = point[0] ** 2 + point[1] ** 2
            if dist < -maxheap[0][0]:
                heappop(maxheap)
                heappush(maxheap, (-dist, [point[0], point[1]]))

        while maxheap:
            res.append(maxheap.pop()[1])

        return res

points = [[1,3],[-2,2]]
K = 1
print(Solution().kClosest(points, K))

points = [[3,3],[5,-1],[-2,4]]
K = 2
print(Solution().kClosest(points, K))
