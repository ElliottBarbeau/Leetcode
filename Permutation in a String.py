def find_permutation(s, pattern):
    window_start = 0
    d = {}
    window_size = len(pattern)

    pattern_freq = {}
    for char in pattern:
        if char not in pattern_freq:
            pattern_freq[char] = 0
        pattern_freq[char] += 1

    for window_end in range(len(s)):
        if s[window_end] not in d:
            d[s[window_end]] = 0
        d[s[window_end]] += 1

        if window_end - window_start + 1 > window_size:
            d[s[window_start]] -= 1
            if d[s[window_start]] == 0:
                del d[s[window_start]]
            window_start += 1
            
        if pattern_freq == d:
            return True

    return False

print(find_permutation('aaacb', 'abc'))