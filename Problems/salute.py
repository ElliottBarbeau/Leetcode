def solution(l):
    new_list = [s.split('.') for s in l]
    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            new_list[i][j] = int(new_list[i][j])

    new_list = sorted(new_list)

    for i in range(len(new_list)):
        for j in range(len(new_list[i])):
            new_list[i][j] = str(new_list[i][j])

    return ['.'.join(new_list[i]) for i in range(len(new_list))]

print(solution(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]))