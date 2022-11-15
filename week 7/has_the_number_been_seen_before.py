lst = list(map(int, input().split()))
mySet = set()
for i in range(len(lst)):
    if lst[i] in mySet:
        print("YES")
    else:
        print("NO")
        mySet.add(lst[i])
