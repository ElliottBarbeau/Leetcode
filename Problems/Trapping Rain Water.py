class Solution:
    def trap(self, height):
        n = len(height)
        if n < 3:
            return 0

        total = 0
        i, j = 0, n-1
        lmax, rmax = height[i], height[j]

        while i <= j:
            lmax, rmax = max(lmax, height[i]), max(rmax, height[j])

            if lmax <= rmax:
                total += (lmax - height[i])
                i += 1

            elif rmax <= lmax:
                total += (rmax - height[j])
                j -= 1
        return total



print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
#height = [0,1,0,2,1,0,1,3,2,1,2,1]