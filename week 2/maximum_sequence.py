n = int(input())
max_n = n
while n != 0:
    n = int(input())
    if max_n < n:
        max_n = n
print(max_n)
