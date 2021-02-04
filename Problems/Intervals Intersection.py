def merge(intervals_a, intervals_b):
    result = []
    a, b = 0, 0
    while a < len(intervals_a) and b < len(intervals_b):
        aint, bint = intervals_a[a], intervals_b[b]
        a_overlaps_b = aint[0] >= bint[0] and aint[0] <= bint[1]

        b_overlaps_a = bint[0] >= aint[0] and bint[0] <= aint[1]

        if a_overlaps_b or b_overlaps_a:
            start = max(aint[0], bint[0])
            end = min(aint[1], bint[1])
            result.append([start, end])   

        if aint[1] < bint[1]:
            a += 1
        else:
            b += 1
    return result


def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()