def factorial(n):
    if n < 0:
        raise ValueError("n must be positive integer number")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
