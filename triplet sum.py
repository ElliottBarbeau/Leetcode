def search_triplets(arr):
    triplets = []
    arr.sort()

    for i in range(len(arr) - 2):
        if arr[i] == arr[i+1]:
            continue
        left, right = i + 1, len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1   
                right -= 1
            else:
                if sum < 0:
                    while arr[left] == arr[left+1]:
                        left += 1
                    left += 1
                else:
                    while arr[right] == arr[right - 1]:
                        right -= 1
                    right -= 1

    return triplets

def main():
    print(search_triplets([-3, 0, 1, 2, -1, 1, -2]))
    print(search_triplets([-5, 2, -1, -2, 3]))

main()