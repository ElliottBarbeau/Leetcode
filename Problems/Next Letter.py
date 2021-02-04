def search_next_letter(letters, key):
    left, right = 0, len(letters) - 1
    if key >= letters[-1] or key > letters[right]:
        return letters[0]

    while left <= right:
        middle = left + (right - left) // 2
        if key >= letters[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return letters[left]


def main():
    print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
    print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
