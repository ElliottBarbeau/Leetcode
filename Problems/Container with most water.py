#Container with most water
#Time complexity: O(N)
#Space complexity: O(1) constant space, only integer variables used, no dict/array etc storing 'n' values
class Solution:
    def maxArea(self, height):
        if len(height) < 2:
            return 0
        maxarea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            maxarea = max(maxarea, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea

#outputs 49
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))