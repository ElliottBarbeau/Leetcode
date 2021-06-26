class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        dp1, dp2 = [0]*n, [nums[0]] + [0]*(n-1)

        for k in range(1, n):
            dp1[k] = max(dp2[k-1] - nums[k], dp1[k-1])
            dp2[k] = max(dp1[k-1] + nums[k], dp2[k-1])

        return max(dp1[-1], dp2[-1])