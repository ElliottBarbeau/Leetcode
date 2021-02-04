#input array = [2, 7, 11, 15] target = 9
#input array2 = [3, 2, 4] target = 6



def two_sum1(array, target):
    for i in array:
        for j in array:
            if array[i] + array[j] == target and i != j:
                return [i, j]

#runtime O(n^2)
#space O(1)


def two_sum2(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        s = array[left] + array[right]
        if s == target:
            return [left, right]
        elif s > target:
            right -= 1
        else:
            left += 1

#runtime O(nlogn)
#space O(1)

        
def two_sum3(array, target):
    seen = {}
    for i in range(len(array)):
        seen[array[i]] = i

    for i in range(len(array)):
        comp = target - array[i]
        if comp in seen:
            return(i, seen[comp])

#runtime O(2n) -> O(n)
#space O(n)

def two_sum4(array, target):
    seen = {}
    for i in range(len(array)):
        comp = target - array[i]
        if comp in seen:
            return(i, seen[comp])
        else:
            seen[array[i]] = i

