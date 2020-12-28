def find_duplicate(nums):
    i = 0
    while i < len(nums):
        if nums[i] != i+1:
            j = nums[i] - 1
            if nums[i] == nums[j]:
                return nums[i]
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()