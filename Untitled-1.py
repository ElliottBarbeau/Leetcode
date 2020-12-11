class Solution:
    def findMin(self, nums) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return nums[i]
        return nums[0]

print(Solution().findMin([1, 2, 3, 4]))