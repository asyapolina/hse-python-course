def sum_of_seq(a):
    res = 0
    if a != 0:
        res += a
    return res


a = int(input())
summa = 0
while a != 0:
    summa += sum_of_seq(a)
    a = int(input())
print(summa)
