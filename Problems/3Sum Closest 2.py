class Solution:
    def threeSumClosest(self, nums, target):
        ans = float('inf')
        closest = float('inf')
        nums.sort()
        
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if s - target == 0:
                    return s
                elif abs(s - target) < closest:
                    closest = abs(s - target)
                    ans = s
                
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
        
        return ans

print(Solution().threeSumClosest([40, 60, -20, -15, 40], 45))