def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1

    return nums
print(cyclic_sort([1, 5, 6, 4, 3, 2]))