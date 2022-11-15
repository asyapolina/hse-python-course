n = int(input())
i = 0
if n % 2 == 0 and n != 0:
    i += 1
while n != 0:
    n = int(input())
    if n % 2 == 0 and n != 0:
        i += 1
print(i)
