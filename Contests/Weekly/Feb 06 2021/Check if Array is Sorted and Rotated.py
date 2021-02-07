class Solution:
    def check(self, nums):
        inflection = False
        for i in range(len(nums)-1):
            if inflection and (nums[i] > nums[0] or nums[i] > nums[i + 1]):
                return False
            if nums[i] > nums[i+1]:
                inflection = True
            
        return True

print(Solution().check([3,4,5,1,2]))
print(Solution().check([2, 1, 3, 4]))
print(Solution().check([1, 2, 3]))
print(Solution().check([1, 1, 1]))
print(Solution().check([2, 1]))
print(Solution().check([8,5,4,5,1,4,5,2,2]))