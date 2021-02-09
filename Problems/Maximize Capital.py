from heapq import heappush, heappop

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    for i in range(len(capital)):
        my_capital = capital[i]
        heappush(minCapitalHeap, (my_capital, i))

    availableCapital = initialCapital
    for _ in range(numberOfProjects):
        while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
            i = heappop(minCapitalHeap)[1]
            profit = profits[i]
            heappush(maxProfitHeap, (-profit, i))

        if not maxProfitHeap:
            break
        availableCapital += -heappop(maxProfitHeap)[0]
    return availableCapital


def main():

    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
