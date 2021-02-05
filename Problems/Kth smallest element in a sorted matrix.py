from heapq import *
class Solution:
    def kthSmallest(self, matrix, k):
        maxheap = []
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if len(maxheap) < k:
                    heappush(maxheap, -matrix[row][column])
                else:
                    if matrix[row][column] < -maxheap[0]:
                        heappushpop(maxheap, -matrix[row][column])

        return -maxheap[0]




print(Solution().kthSmallest([[0,0,0],[2,7,9],[7,8,11]], 7))
print(Solution().kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8))