class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        s /= 2
        
        dp = [[False for _ in range(s + 1)] for _ in range(len(nums) + 1)]

        dp[0][0] = True
        for i in range(1, len(nums) + 1):
            dp[i][0] = True
        
        for i in range(1, sum + 1):
            dp[0][i] = False

        for i in range(1, len(nums) + 1):
            for j in range(1, s + 1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j - nums[i - 1]]

        return dp[len(nums)][sum]
