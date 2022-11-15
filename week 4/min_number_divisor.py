import math


def MinDivisor(n):
    a = n
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            a = i
            break
    return a


num = int(input())
print(MinDivisor(num))
