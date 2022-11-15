n = int(input())
eq_n = 1
i = 0
j = 0
while n != 0:
    if n == eq_n:
        j += 1
        if j > i:
            i = j
        else:
            eq_n = n
            # как обнулить(до 1?) счетчик
    n = int(input())
print(j)
