def fruits_into_baskets(fruits):
    # TODO: Write your code here
    fruit_count = {}
    windowStart = 0
    max_length = float('-inf')

    for windowEnd in range(len(fruits)):
        if fruits[windowEnd] not in fruit_count:
            fruit_count[fruits[windowEnd]] = 0
        fruit_count[fruits[windowEnd]] += 1

        while len(fruit_count) > 2:
            fruit_count[fruits[windowStart]] -= 1
            if fruit_count[fruits[windowStart]] == 0:
                del fruit_count[fruits[windowStart]]
            windowStart += 1

        max_length = max(max_length, windowEnd - windowStart + 1)

    return max_length

print(fruits_into_baskets([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))