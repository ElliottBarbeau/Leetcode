class Solution:
    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
            
        return ans

print(Solution().singleNumber([4,1,2,1,2]))