import math 
def findIndex(n) : 
    fibo = 2.078087 * math.log(n) + 1.672276
   
    # returning rounded off value of index 
    return round(fibo) - 2

def main():
    m = 4
    f = 7
    '''
    if m >= f:
        print(findIndex(m))
    else:
         print(findIndex(f))
'''
    m = 99
    f = 199
    print(findIndex(m))
    print(findIndex(f))

main()

#1, 1, 2, 3, 5, 8, 13, 21, 34, 55

#1, 1
#2, 1
#2, 3
#5, 3
#5, 8
#13, 8
#13, 21
