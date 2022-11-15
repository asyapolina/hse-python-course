def merge(a, b):
    c = a + b
    return sorted(c)

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
print(*merge(lst1, lst2))
