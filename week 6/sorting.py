n = int(input())
if n <= 10 ** 5:
    lst = list(map(int, input().split()))
    lst_new = sorted(lst)
print(*lst_new)
