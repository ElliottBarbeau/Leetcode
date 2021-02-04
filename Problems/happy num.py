class Solution:
    def isHappy(self, n: int) -> bool:
        fast, slow = n, n
        while True:
            fast = self.calc(self.calc(fast))
            slow = self.calc(slow)
            if fast == 1:
                return True

            if fast == slow:
                break
            
        return False

        
        
    def calc(self, num):
        s = str(num)
        total = 0
        for char in s:
            total += int(char) ** 2
            
        print(total)
        return total

print(Solution().isHappy(19))