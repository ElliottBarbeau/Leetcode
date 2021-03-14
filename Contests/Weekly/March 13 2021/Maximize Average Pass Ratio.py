from heapq import heappop, heappush
class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        maxheap = []
        
        for i in range(len(classes)):
            c = classes[i]
            if c[0] / c[1] != 1:
                heappush(maxheap, (-(((c[0] + 1) / (c[1] + 1)) - (c[0] / c[1])), i))

        if not maxheap:
            return 1

        while extraStudents > 0:
            temp = list(heappop(maxheap))
            c = classes[temp[1]]
            classes[temp[1]][0] += 1
            classes[temp[1]][1] += 1
            temp[0] = -(((c[0] + 1) / (c[1] + 1)) - (c[0] / c[1]))
            heappush(maxheap, tuple(temp))
            extraStudents -= 1

        total = 0
        for clas in classes:
            total += clas[0] / clas[1]

        return total / len(classes)