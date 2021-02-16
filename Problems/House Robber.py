# Top down memoization
'''
class Solution:
    def rob(self, nums) -> int:
        memo = [-1] * (len(nums) + 1)
        return self.dp(nums, len(nums) - 1, memo)
    
    def dp(self, nums, index, memo):
        if index < 0:
            return 0
        if memo[index] >= 0:
            return memo[index]
        
        memo[index] = max(self.dp(nums, index - 2, memo) + nums[index], self.dp(nums, index - 1, memo))
        
        return memo[index]
    
nums = [1,2,3,1]
print(Solution().rob(nums))
'''

# Iterative bottom up memoization
class Solution:
    def rob(self, nums) -> int:
        memo = [-1] * (len(nums) + 1)
        if not nums:
            return 0
        memo[0] = 0
        memo[1] = nums[0]

        for i in range(1, len(nums)):
            memo[i + 1] = max(memo[i - 1] + nums[i], memo[i])

        return memo[len(nums)]

nums = [1,2,3,1]
print(Solution().rob(nums))