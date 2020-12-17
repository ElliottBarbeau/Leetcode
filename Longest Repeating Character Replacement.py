def length_of_longest_substring(s, k):
    windowStart, max_length, max_repeat_letter_count = 0, 0, 0
    frequency_map = {}

    for windowEnd in range(len(s)):
        right_char = s[windowEnd]
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])

        if (windowEnd - windowStart + 1 - max_repeat_letter_count) > k:
            left_char = s[windowStart]
            frequency_map[left_char] -= 1
            windowStart += 1

        max_length = max(max_length, windowEnd - windowStart + 1)

    return max_length

print(length_of_longest_substring('aabccbb', 2))