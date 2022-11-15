import itertools

print(any(list(map(lambda x: x == int(input()), itertools.repeat(0, int(input()))))))