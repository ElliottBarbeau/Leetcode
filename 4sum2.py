class Solution:
    #[1,0,-1,0,-2,2]
    #[-2, -1, 0, 0, 1, 2]
    def fourSum(self, nums, target):
        nums.sort()
        i = 0
        ret = []
        while i < len(nums) - 3:
            j = i + 1
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            while j < len(nums) - 2:
                if nums[j] == nums[j - 1]:
                    j += 1
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    s = nums[i] + nums[j] + nums[left] + nums[right]
                    if s == target:
                        ret.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right > 0 and nums[right] == nums[right - 1]:
                            nums -= 1
                        left += 1
                        right -= 1
                    elif s < target:
                        left += 1
                    else:
                        right -= 1

                j += 1
            i += 1
            
        return ret

print(Solution().fourSum([1,0,-1,0,-2,2], 0))