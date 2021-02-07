class Solution:
    def sumOfUnique(self, nums):
        d = {}
        total = 0
        
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
            
        for num in d:
            if d[num] == 1:
                total += num
                
        return total