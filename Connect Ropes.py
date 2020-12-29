from heapq import *
import heapq

def minimum_cost_to_connect_ropes(ropeLengths):
    heapify(ropeLengths)
    result = 0

    while ropeLengths:
        num1 = heappop(ropeLengths)
        num2 = heappop(ropeLengths)
        num3 = num1 + num2
        result += num3
        if ropeLengths:
            heappush(ropeLengths, num3)

    return result


def main():

    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
