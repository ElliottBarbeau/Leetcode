def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr)-1

    while left<right:
        if arr[left] + arr[right] < target_sum:
            left += 1
        elif arr[left] + arr[right] > target_sum:
            right -= 1
        else: return [left, right]
    return [-1, -1]