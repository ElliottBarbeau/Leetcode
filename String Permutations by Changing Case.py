def find_letter_case_string_permutations(str):
    permutations = []
    permutations.append(str)

    i = 0
    while i < len(str):
        if str[i].isdigit():
            i += 1
            continue
        for j in range(len(permutations)):
            permutations.append(swap_nth(permutations[j], i))

        i += 1
    return permutations

def swap_nth(s, n):
    temp = list(s)
    temp[n] = temp[n].swapcase()
    return ''.join(temp)

def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("Ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


main()
