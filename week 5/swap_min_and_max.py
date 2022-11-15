lst = list(map(int, input().split()))
indx_min = 0
indx_max = -1
min_el = lst[0]
max_el = lst[-1]
for i in range(len(lst)):
    if lst[i] < min_el:
        min_el = lst[i]
        indx_min = i
    if lst[i] > max_el:
        max_el = lst[i]
        indx_max = i
lst[indx_min], lst[indx_max] = lst[indx_max], lst[indx_min]
print(*lst)
