import math
x = float(input())
if (x % 1) >= 0.5:
    print(int(math.ceil(x)))
else:
    print(int(math.floor(x)))
