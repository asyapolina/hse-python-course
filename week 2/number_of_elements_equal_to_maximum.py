n = int(input())
max_n = 1
i = 0
while n != 0:
    if n == max_n:
        i += 1
    if n > max_n:
        max_n = n
        i = 1
    n = int(input())
print(i)
