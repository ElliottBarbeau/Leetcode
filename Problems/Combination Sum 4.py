class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]

        return dp[target]

nums = [1, 2, 3]
target = 4
print(Solution().combinationSum4(nums, target))