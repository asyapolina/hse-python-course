n = list(map(int, input().split()))
s = 0
i = n[0]
for j, max_num in enumerate(n):
    if max_num >= s:
        s = max_num
        i = j
print(s, i)
