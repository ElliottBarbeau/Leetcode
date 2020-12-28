def find_subsets(nums):
  subsets = []
  
  subsets.append([])
  for i in range(len(nums)):
      n = len(subsets)
      for j in range(n):
          copy = list(subsets[j])
          copy.append(nums[i])
          subsets.append(copy)

  return subsets


def main():

  print("Here is the list of subsets: " + str(find_subsets([1, 3])))
  print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()
