n = int(input())
s = list(map(int, input().split()))
x = int(input())
first = s[0]
for i in s:
    if abs(i - x) < abs(first - x):
        first = i
print(first)
