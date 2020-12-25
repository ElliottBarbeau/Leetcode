def remove_duplicates(arr):
    n = len(arr)
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            n -= 1
    return n