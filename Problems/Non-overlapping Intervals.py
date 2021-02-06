class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()

        last_end = intervals[0][0]
        non_overlapping = 0
        for interval in intervals:
            if last_end > interval[0]:
                last_end = min(last_end, interval[1])
            else:
                non_overlapping += 1
                last_end = interval[1]

        return len(intervals) - non_overlapping

print(Solution().eraseOverlapIntervals([[1,100],[11, 22],[1, 11],[1, 12]]))
print(Solution().eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
print(Solution().eraseOverlapIntervals([[1,2],[2,3]]))
