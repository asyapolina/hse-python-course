a = float(input())
b = float(input())
c = float(input())
if a > 0 and b > 0 and c > 0:
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** (1/2)
    print(area)
