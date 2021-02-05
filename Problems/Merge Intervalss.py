class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key = lambda x: x[0])
        result = []

        start = intervals[0][0]
        end = intervals[0][1]
        for interval in intervals:
            new_start = interval[0]
            new_end = interval[1]
            if new_start <= end:
                end = max(end, new_end)
            else:
                result.append([start, end])
                start = new_start
                end = new_end

        result.append([start, end])
        return result

print(Solution().merge([[1,4],[0,4]]))
print(Solution().merge([[1,4],[2,3]]))
print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))