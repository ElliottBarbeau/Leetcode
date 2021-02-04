def length_of_longest_substring(arr, k):
    freq, window_start, max_length = 0, 0, 0

    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            freq += 1

        if window_end - window_start + 1 - freq > k:
            if arr[window_start] == 1:
                freq -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

print(length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))