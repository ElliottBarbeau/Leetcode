class Solution:
    def missingNumber(self, nums):
        total = 0
        range_total = 0

        for i in range(len(nums) + 1):
            range_total += i

        for num in nums:
            total += num

        return(range_total - total)


print(Solution().missingNumber([0, 1, 2, 4]))