n = int(input())
max_el = n
second_max_el = 1
while n != 0:
    n = int(input())
    if n != 0:
        if max_el <= n:
            second_max_el = max_el
            max_el = n
        if second_max_el < n < max_el:
            second_max_el = n
print(second_max_el)
