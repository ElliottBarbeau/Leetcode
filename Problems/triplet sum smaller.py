def triplet_with_smaller_sum(arr, target):
    count = 0
    arr.sort()
    
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count

def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))


main()