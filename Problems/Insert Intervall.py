class Solution:
    def insert(self, intervals, newInterval):
        intervals.sort()
        if not intervals:
            return [newInterval]
        res = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        res.append([newInterval[0], newInterval[1]])

        while i < len(intervals) and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1

        return res

intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(Solution().insert(intervals, newInterval))
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(Solution().insert(intervals, newInterval))