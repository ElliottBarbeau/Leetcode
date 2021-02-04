class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        for i in range(lowLimit, highLimit + 1):
            curr = 0
            num = str(i)
            for char in num:
                curr += int(char)
                
            if curr not in d:
                d[curr] = 0
            d[curr] += 1
            
        return max(d.values())