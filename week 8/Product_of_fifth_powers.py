import functools


print(functools.reduce(lambda x,y: x*y**5, [1] + list(map(int, input().split()))))
