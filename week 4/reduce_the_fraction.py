import math


def FractionReduction(n, m):
    q = math.gcd(n, m)
    return int(n / q), int(m / q)


n, m = int(input()), int(input())
print(*FractionReduction(n, m))
