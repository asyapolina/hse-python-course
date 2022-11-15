import math


def SimpleNumber(n):
    count = 0
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
    if count > 0:
        return False
    else:
        return True


num = int(input())
if SimpleNumber(num):
    print("YES")
else:
    print("NO")
