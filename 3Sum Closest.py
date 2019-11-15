class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = (nums[0] + nums[1] + nums[2])
        for i in range(len(nums)-2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s == result:
                    return result
                
                if abs(s - target) < abs(result - target):
                    result = s

                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
        return result

target = 1
nums = [-1, 2, 1, -4]
print(Solution().threeSumClosest(nums, target))