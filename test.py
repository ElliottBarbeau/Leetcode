def test(x, y):
    temp = (x - y) // y
    print(temp)
    temp += ((x - y) % y > 0)
    print((x - y) % y > 0)

    return temp


test(19, 10)