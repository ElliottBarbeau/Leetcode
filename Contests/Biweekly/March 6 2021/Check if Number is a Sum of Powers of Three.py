class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def base3(n):
            if n == 0:
                return '0'
            digits = []
            while n > 0:
                n, remainder = divmod(n, 3)
                digits.append(str(remainder))

            digits[::-1]
            return ''.join(digits)
        
        s = base3(n)
        for char in s:
            if char != '1' and char != '0':
                return False
            
        return True