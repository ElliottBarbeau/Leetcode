#Reverse an integer
def reverse(num):
    output = 0
    while num > 0:
        output *= 10
        output += num % 10
        num //= 10
    return output

print(reverse(123))