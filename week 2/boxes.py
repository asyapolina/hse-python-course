A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
a = sorted([A1, B1, C1])
b = sorted([A2, B2, C2])
if a == b:
    print("Boxes are equal")
elif a[0] <= b[0] and a[1] <= b[1] and a[2] <= b[2]:
    print("The first box is smaller than the second one")
elif a[0] >= b[0] and a[1] >= b[1] and a[2] >= b[2]:
    print("The first box is larger than the second one")
else:
    print("Boxes are incomparable")
