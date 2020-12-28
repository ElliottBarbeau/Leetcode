def find_corrupt_numbers(nums):
    i, n = 0, len(nums)
    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        else:
            i += 1

    for i in range(n):
        if nums[i] != i+1:
            return[nums[i], i + 1]
