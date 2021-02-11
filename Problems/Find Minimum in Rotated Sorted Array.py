class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[left] > nums[right]:
                if nums[left] > nums[right]:
                    if nums[mid] > nums[right]:
                        left = mid + 1
                    elif nums[left] > nums[mid]:
                        right = mid
            else:
                break
            
        return nums[left]

print(Solution().findMin([4,5,6,7,0,1,2]))