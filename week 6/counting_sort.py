def CountSort(A):
    lst_int = [0] * 101
    res = ""
    for now in A:
        lst_int[now] += 1
    for i in range(len(lst_int)):
        res += (str(i) + " ") * lst_int[i]
    return res

myList = list(map(int, input().split()))
print(CountSort(myList))
