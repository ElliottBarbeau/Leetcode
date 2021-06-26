class Solution:
    def maxDistToClosest(self, seats: list[int]) -> int:
        m = 1
        prev = -1
        for i, seat in enumerate(seats):
            if seat == 1:
                if -1 == prev:
                    m = max(m, i - prev - 1)
                else:
                    m = max(m, (i - prev) // 2)
                prev = i

        m = max(len(seats) - prev - 1, m)
        return m
