class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        running_total = window_start = 0
        ret = float('inf')
        for window_end in range(len(nums)):
            running_total += nums[window_end]
            while running_total >= target:
                ret = min(ret, window_end - window_start + 1)
                running_total -= nums[window_start]
                window_start += 1

        return 0 if ret == float('inf') else ret
