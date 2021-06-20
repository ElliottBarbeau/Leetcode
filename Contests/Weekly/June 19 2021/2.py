class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        if startTime == finishTime:
            return 0

        startTime = startTime.split(":")
        finishTime = finishTime.split(":")
        
        s0 = int(startTime[0])
        s1 = int(startTime[1])
        f0 = int(finishTime[0])
        f1 = int(finishTime[1])

        if abs((s0 * 60 + s1) - (f0 * 60 + f1)) < 15 and f1 > s1:
            return 0
        
        while s1 % 15 != 0:
            s1 += 1
            
        if s1 == 60:
            s0 += 1
            s1 = 0
            
        while f1 % 15 != 0:
            f1 -= 1
            
        if f1 == 60:
            f0 += 1
            f1 = 0
            
        if s0 > f0 or (s0 == f0 and s1 > f1):
            f0 += 24
        return (f0 - s0) * 4 + (f1 - s1) // 15

startTime = "04:54"
finishTime = "18:51"

print(Solution().numberOfRounds(startTime, finishTime))

startTime = "18:51"
finishTime = "04:54"

print(Solution().numberOfRounds(startTime, finishTime))

startTime = "10:10"
finishTime = "10:11"
print(Solution().numberOfRounds(startTime, finishTime))

startTime = "00:01"
finishTime = "00:00"
print(Solution().numberOfRounds(startTime, finishTime))