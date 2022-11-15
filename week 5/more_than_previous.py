s = list(map(int, input().split()))
lst = []
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        lst.append(s[i])
print(*lst)
