from collections import deque
def find_permutations(nums):
    result = []

    n = len(nums)
    permutations = deque()
    permutations.append([])
    for curr_num in nums:
        p = len(permutations)
        for _ in range(p):
            oldPermutation = permutations.popleft()
            for j in range(len(oldPermutation) + 1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, curr_num)
                if len(newPermutation) == n:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)
    
    return result


def main():
    print("Here are all the permutations: " +
          str(find_permutations([1, 3, 5])))


main()
