def search_quadruplets(arr, target):
    quadruplets = []
    arr.sort()
    n = len(arr)
    for i in range(n-3):
        j = i + 1
        if arr[i] == arr[i+1]:
            continue
        while j < n - 2:
            if arr[j] == arr[j - 1] and j < n - 2:
                j += 1
                continue
            left, right = j + 1, n - 1
            while left < right:
                sum = arr[i] + arr[j] + arr[left] + arr[right]
                if sum == target:
                    quadruplets.append([arr[i], arr[j], arr[left], arr[right]])
                    right -= 1
                    left += 1
                    while left < right and arr[left] == arr[left+1]:
                        left += 1
                    while right > left and arr[right] == arr[right-1]:
                        right -=1
                else:
                    if sum < target:
                        left += 1
                    else:
                        right -= 1
            j += 1
    return quadruplets

print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))

#[-3, -1, 1, 1, 2, 4]