def find_substring(s, pattern):
    window_start = 0
    pattern_freq = {}
    shortest = float('inf')
    ret = ''
    matched = 0

    char_freq = {}

    for char in pattern:
        if char not in pattern_freq:
            pattern_freq[char] = 0
        pattern_freq[char] += 1

    for window_end in range(len(s)):
        if s[window_end] not in char_freq:
            char_freq[s[window_end]] = 0
        char_freq[s[window_end]] += 1

        if s[window_end] in pattern_freq and char_freq[s[window_end]] <= pattern_freq[s[window_end]]:
            matched += 1

        while matched == len(pattern):
            if window_end - window_start + 1 < shortest:
                shortest = window_end - window_start + 1
                ret = s[window_start:window_end + 1]

            if s[window_start] in pattern_freq and char_freq[s[window_start]] <= pattern_freq[s[window_start]]:
                matched -= 1

            char_freq[s[window_start]] -= 1
            window_start += 1

    return ret

print(find_substring('adcad', 'abc'))