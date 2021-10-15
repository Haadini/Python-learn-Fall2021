'''
project euler
first
mazarebe 3 va 5 zire 1000 chia hastan?
onaro ba ham jam kon
'''


def Sum3va5():
    sum = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
            i += 1
    return sum


print(Sum3va5())