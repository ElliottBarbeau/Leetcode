class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        first = self.dp(nums[1:], len(nums) - 2)
        second = self.dp(nums[:len(nums) - 1], len(nums) - 2)
        return max(first, second)

    def dp(self, nums, index):
        memo = [0] * (len(nums) + 1)
        memo[1] = nums[0]
        for i in range(1, len(nums)):
            memo[i + 1] = max(memo[i - 1] + nums[i], memo[i])

        return memo[len(nums)]

nums = [1,2,3,1]

print(Solution().rob(nums))
