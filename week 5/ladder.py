n = int(input())
if n <= 9:
    for i in range(1, n + 1):
        s = ""
        for j in range(1, i + 1):
            s += str(j)
        print(s)
