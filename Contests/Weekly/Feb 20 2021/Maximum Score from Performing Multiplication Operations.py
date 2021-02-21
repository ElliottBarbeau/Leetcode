class Solution:
    def maximumScore(self, nums, multipliers) -> int:
        self.maximum_score = -float('inf')
        nums_pointer_left, nums_pointer_right, multipliers_pointer = 0, len(nums) - 1, 0
        return self.helper(nums_pointer_left, nums_pointer_right, multipliers_pointer, 0, nums, multipliers)
        
    def helper(self, nums_pointer_left, nums_pointer_right, multipliers_pointer, curr_score, nums, multipliers):
        if multipliers_pointer >= len(multipliers):
             self.maximum_score = max(self.maximum_score, curr_score)
             return

        self.helper(nums_pointer_left + 1, nums_pointer_right, multipliers_pointer + 1, curr_score + (nums[nums_pointer_left] * multipliers[multipliers_pointer]), nums, multipliers)
        self.helper(nums_pointer_left, nums_pointer_right - 1, multipliers_pointer + 1, curr_score + (nums[nums_pointer_right] * multipliers[multipliers_pointer]), nums, multipliers)

        return self.maximum_score


nums = [-5,-3,-3,-2,7,1]
multipliers = [-10,-5,3,4,6]
print(Solution().maximumScore(nums, multipliers))