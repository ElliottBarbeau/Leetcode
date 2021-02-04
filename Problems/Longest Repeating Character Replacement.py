def length_of_longest_substring(s, k):
    window_start, max_length, max_repeat = 0, 0, 0
    char_count = {}

    for window_end in range(len(s)):
        if s[window_end] not in char_count:
            char_count[s[window_end]] = 0
        char_count[s[window_end]] += 1

        max_repeat = max(max_repeat, char_count[s[window_end]])

        if window_end - window_start + 1 - max_repeat > k:
            char_count[s[window_start]] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

print(length_of_longest_substring('aabccbb', 2))