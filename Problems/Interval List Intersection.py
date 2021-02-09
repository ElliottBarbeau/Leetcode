class Solution:
    def intervalIntersection(self, firstList, secondList):
        a_pointer = 0
        b_pointer = 0
        if not firstList or not secondList:
            return []

        res = []

        while a_pointer < len(firstList) and b_pointer < len(secondList):
            a = firstList[a_pointer]
            b = secondList[b_pointer]

            if (a[0] <= b[0] and (a[1] >= b[1] or (a[1] >= b[0] and a[1] <= b[1]))) or (b[0] <= a[0] and (b[1] >= a[1] or (b[1] >= a[0] and b[1] <= a[1]))):
                start = max(a[0], b[0])
                end = min(a[1], b[1])
                res.append([start, end])

            if a[1] < b[1]:
                a_pointer += 1
            else:
                b_pointer += 1

        return res

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]
print(Solution().intervalIntersection(firstList, secondList))

firstList = [[1,3],[5,9]]
secondList = []
print(Solution().intervalIntersection(firstList, secondList))

firstList = [[10,12],[18,19]]
secondList = [[1,6],[8,11],[13,17],[19,20]]
print(Solution().intervalIntersection(firstList, secondList))