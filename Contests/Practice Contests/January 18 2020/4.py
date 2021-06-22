class Solution:
    def minTaps(self, n: int, ranges: list[int]) -> int:
        intervals = [(max(i - ranges[i], 0), i + ranges[i]) for i in range(len(ranges))]
        intervals.sort()
        i = 0
        ans = 0
        prev = 0
        while i < len(intervals):
            if prev >= n:
                return ans
            
            m = float('-inf')
            for j in range(i, len(intervals)):
                if intervals[j][0] <= prev:
                    m = max(intervals[j][1], m)
                else:
                    break
                    
            if m == float('-inf'):
                return -1
            
            prev = m
            i = j
            ans += 1
        return ans