def loop(a, b):
    s = a + b
    temp = s
    while temp % 2 == 0:
        temp /= 2
    return (a % temp) != 0