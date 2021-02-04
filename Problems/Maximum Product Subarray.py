class Solution:
    def maxProduct(self, nums) -> int:
        all_zeros = True
        max_product = float('-inf')
        count = 0
        for i in range(len(nums)):
            count = i
            if nums[i] != 0:
                all_zeros = False
            p = 1
            while count <= len(nums) - 1:
                p *= nums[count]
                if p > max_product:
                    max_product = p
                count += 1

                    
        if all_zeros:
            return 0
        else:
            return max_product

print(Solution().maxProduct([-2, 0, -1]))