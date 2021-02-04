def non_repeat_substring(s):
    
    #Non-Dynamic sliding window
    '''
    max_length = float('-inf')
    windowStart = 0
    char_count = {}

    for windowEnd in range(len(s)):
        while s[windowEnd] in char_count:
            char_count[s[windowStart]] -= 1
            if char_count[s[windowStart]] == 0:
                del char_count[s[windowStart]]
            windowStart += 1

        char_count[s[windowEnd]] = 1
        max_length = max(windowEnd - windowStart + 1, max_length)

    return max_length
    '''

    #Dynamic sliding window
    max_length = float('-inf')
    windowStart = 0
    char_count = {}

    for windowEnd in range(len(s)):
        if s[windowEnd] in char_count:
            windowStart = max(windowStart, char_count[s[windowEnd]] + 1)
        
        char_count[s[windowEnd]] = windowEnd
        max_length = max(max_length, windowEnd - windowStart + 1)

    return max_length

print(non_repeat_substring("pwwkewhsjdkgmnhwkferwhw"))