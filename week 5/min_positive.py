s = list(map(int, input().split()))
min_el = 1001
for i in s:
    if i > 0:
        if i < min_el:
            min_el = i
print(min_el)
