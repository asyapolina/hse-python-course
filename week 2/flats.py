n1 = int(input())
n2 = int(input())
if ((n1 - 1) % (n2 - n1 + 1) == 0):
    print("YES")
else:
    print("NO")
