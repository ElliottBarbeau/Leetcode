class Solution(object):
    def findNumberOfLIS(self, nums):
        N = len(nums)
        lengths = [0] * N
        counts = [1] * N

        for j in range(len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

nums = [1]
print(Solution().findNumberOfLIS(nums))