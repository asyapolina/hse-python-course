A, B, C = int(input()), int(input()), int(input())
D, E = int(input()), int(input())
if (A <= D and B <= E) or (A <= E and B <= D) \
    or (B <= D and C <= E) or (B <= E and C <= D) \
        or (A <= D and C <= E) or (A <= E and C <= D):
    print("YES")
else:
    print("NO")
