class Solution:
    def findTargetSumWays(self, nums, S) -> int:
        memo = {}
        return self.dp(nums, S, memo, 0, len(nums) - 1)

    def dp(self, nums, target, memo, curr_sum, index):
        if index < 0 and target == curr_sum:
            return 1
        
        if index < 0:
            return 0

        if (index, curr_sum) in memo:
            return memo[index, curr_sum]

        positive = self.dp(nums, target, memo, curr_sum + nums[index], index - 1)
        negative = self.dp(nums, target, memo, curr_sum - nums[index], index - 1)

        total = positive + negative
        memo[(index, curr_sum)] = total
        return memo[(index, curr_sum)]
        
