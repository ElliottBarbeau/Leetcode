def triplet_sum_close_to_target(arr, target_sum):
    closest = float('inf')
    ans = 0
    arr.sort()
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            if abs(arr[i] + arr[left] + arr[right] - target_sum) < closest:
                closest = abs(arr[i] + arr[left] + arr[right] - target_sum)
                ans = arr[i] + arr[left] + arr[right]
            
            if arr[i] + arr[left] + arr[right] == target_sum:
                return arr[i] + arr[left] + arr[right]
            else:
                if arr[i] + arr[left] + arr[right] > target_sum:
                    right -= 1
                else:
                    left += 1
    return ans

def main():
  print(triplet_sum_close_to_target([-2, 0, 1, 2], 2))
  print(triplet_sum_close_to_target([-3, -1, 1, 2], 1))
  print(triplet_sum_close_to_target([1, 0, 1, 1], 100))


main()