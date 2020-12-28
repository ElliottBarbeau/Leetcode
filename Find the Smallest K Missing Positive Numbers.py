def find_first_k_missing_positive(nums, k):
    missingNumbers = []
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    l = 0
    extraNumbers = set()
    while l < n and k > 0:
        if nums[l] != l + 1:
            k -= 1
            missingNumbers.append(l + 1)
            extraNumbers.add(nums[l])
        l += 1

    m = max(nums) + 1
    while k > 0:
        if m not in extraNumbers:
            missingNumbers.append(m)
            m += 1
            k -= 1

    return missingNumbers

print(find_first_k_missing_positive([2, 3, 4], 3))