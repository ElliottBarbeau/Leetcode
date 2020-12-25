def backspace_compare(str1, str2):
    index1, index2 = len(str1) - 1, len(str2) - 1

    while (index1 >= 0 or index2 >= 0):
        index1 = get_next_valid_char(str1, index1)
        index2 = get_next_valid_char(str2, index2)
        if index1 < 0 and index2 < 0:
            return True
        if str1[index1] != str2[index2]:
            return False
        if index1 < 0 or index2 < 0:
            return False

        index1 -= 1
        index2 -= 1

    return True


def get_next_valid_char(s, index):
    backspace_count = 0
    while index >= 0:
        if s[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break

        index -= 1

    return index

print(backspace_compare("xywrrmp", "xywrrmu#p"))

