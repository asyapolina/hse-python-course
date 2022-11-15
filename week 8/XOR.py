print(*map(lambda s: s[0] ^ s[1], zip(map(int, input().split()), map(int, input().split()))))
