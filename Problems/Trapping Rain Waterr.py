class Solution:
    def trap(self, height) -> int:
        if not height:
            return 0
        total = 0
        left = [height[0]] * len(height)
        right = [height[-1]] * len(height)
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
            
        for i in reversed(range(len(height)-1)):
            right[i] = max(height[i], right[i + 1])
            
        for i in range(len(height)):
            total += min(left[i], right[i]) - height[i]
            
        return total