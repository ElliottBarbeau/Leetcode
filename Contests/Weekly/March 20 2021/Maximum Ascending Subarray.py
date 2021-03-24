class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        overall_max, curr_sum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curr_sum += nums[i]
            else:
                curr_sum = nums[i]
                
            overall_max = max(curr_sum, overall_max)
        return overall_max