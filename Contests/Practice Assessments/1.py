class Solution:
    def rotatedDigits(self, n: int) -> int:
        l = ['2', '5', '6', '9']
        banned = ['3', '4', '7']
        count = 0
        for num in range(1, n + 1):
            flag = False
            for char in str(num):
                if char in l:
                    flag = True
                if char in banned:
                    flag = False
                    break
            count += flag
                
                    
        return count

print(Solution().rotatedDigits(850))