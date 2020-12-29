from heapq import *

def sort_character_by_frequency(str):
    maxHeap = []
    frequency_map = {}
    ret = ""

    for char in str:
        if char not in frequency_map:
            frequency_map[char] = 0
        frequency_map[char] += 1

    for key in frequency_map.keys():
        heappush(maxHeap, (-frequency_map[key], key))

    while maxHeap:
        freq, char = heappop(maxHeap)
        ret += char * -freq

    return ret


def main():

    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
