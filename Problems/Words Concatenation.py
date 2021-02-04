def find_word_concatenation(str1, words):
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    words_length = len(words[0])

    for i in range(words_length + 1):
        words_seen = {}
        for j in range(0, words_count):
            next_word_index = i + j * words_length
            word = str1[next_word_index: next_word_index + words_length]
            if word not in word_frequency:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            if words_seen[word] > word_frequency.get(word, 0):
                break
        
            if j + 1 == words_count:
                result_indices.append(i)


    return result_indices

print(find_word_concatenation("catfoxcat", ["cat", "fox"]))