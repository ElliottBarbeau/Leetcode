class Solution:
    def maximumTime(self, time: str) -> str:
        
        newstr = ''
        temp = '456789'
        
        for i in range(len(time)):
            if time[i] == '?':
                if i == 0:
                    if time[1] in temp:
                        newstr += '1'
                    else:
                        newstr += '2'
                elif i == 1:
                    if time[0] == '?' or time[0] == '2':
                        newstr += '3'
                    else:
                        newstr += '9'
                elif i == 2:
                    newstr += ':'
                elif i == 3:
                    newstr += '5'
                elif i == 4:
                    newstr += '9'
            else:
                newstr += time[i]
        
        return newstr

print(Solution().maximumTime('2?:3'))