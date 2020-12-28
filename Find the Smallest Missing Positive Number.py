def find_first_missing_positive(nums):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] <= 0:
            i += 1
            continue
        
        if nums[i] < n and nums[i] != i + 1:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1

print(find_first_missing_positive([-3, 1, 5, 4, 2]))
print(find_first_missing_positive([3, -2, 0, 1, 2]))
print(find_first_missing_positive([1, 2, 3, 4]))