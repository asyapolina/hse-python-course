n = int(input())
s = set()
m = set()
while True:
    input1 = input()
    if input1 == "HELP":
        break
    lst1 = map(int, input1.split())
    ans = input()
    if ans == "YES":
        if len(m) == 0:
            m = set(lst1)
        else:
            m &= set(lst1)
    if ans == "NO":
        s |= set(lst1)
if (len(m) != 0):
    print(*sorted(list(m - s)))
else:
    print(*sorted(list(set(range(1, n + 1)) - s)))
