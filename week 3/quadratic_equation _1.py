a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
x2 = (- b + d ** (1 / 2)) / (2 * a)
x1 = (- b - d ** (1 / 2)) / (2 * a)
if d > 0:
    if x1 < x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif d == 0:
    print(x1)
