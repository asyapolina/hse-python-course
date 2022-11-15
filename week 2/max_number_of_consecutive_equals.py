n = int(input())
count = 0
max_num = 0
a = n
while n != 0:
    if a == n:
        count += 1
        if max_num < count:
            max_num = count
    else:
        count = 1
        a = n
    n = int(input())
print(max_num)
