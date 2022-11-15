def fast_exponent(a, n):
    if n == 1:
        return a
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_exponent(a ** 2, n / 2)
    return a * fast_exponent(a, n - 1)


num, exp = float(input()), int(input())
print(fast_exponent(num, exp))
