class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        output = []
        i = 0
        while i < n:
            j = nums[i] - 1
            print(nums)
            if nums[i] <= n and nums[i] != nums[j] and nums[i] != i + 1:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
                
        
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                output.append(i + 1)
                
        return output

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))