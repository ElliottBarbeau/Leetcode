def find_happy_number(num):
    fast, slow = num, num
    while fast != 1:
        fast = helper(helper(fast))
        slow = helper(slow)

        if fast == slow:
            return False

    return True

def helper(num):
    temp = 0
    a = str(num)
    for num in a:
        temp += int(num)**2
    return temp

def main():
    print(find_happy_number(23))
    print(find_happy_number(12))


main()