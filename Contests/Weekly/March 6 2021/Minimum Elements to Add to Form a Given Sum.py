class Solution:
    def minElements(self, nums: list[int], limit: int, goal: int) -> int:
        s = sum(nums)
        total = 0
        remainder = 1
        if (abs(goal - s) % limit) == 0:
            remainder = 0
        total += (abs(goal - s) // limit)
            
        return total if remainder == 0 else total + 1

nums, limit, goal = [-1, 0, 1, 1, 1], 1, 771843707
print(Solution().minElements(nums, limit, goal))

nums = [1,-10,9,1]
limit = 100
goal = 0
print(Solution().minElements(nums, limit, goal))