x, y = int(input()), int(input())
summa = x
i = 1
while summa < y:
    summa += (summa * 0.1)
    i += 1
    if summa > y:
        break
print(i)
