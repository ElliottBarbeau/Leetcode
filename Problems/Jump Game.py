class Solution:
    def canJump(self, nums: list[int]):
        last = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last:
                last = i

        return last == 0

print(Solution().canJump([3, 2, 1, 0, 4]))