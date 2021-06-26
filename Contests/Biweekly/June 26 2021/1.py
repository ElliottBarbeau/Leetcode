class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            t = nums[:i] + nums[i+1:]
            if all(t[i] < t[i+1] for i in range(len(t)-1)):
                return True
            
        return False