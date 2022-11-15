n = int(input())
myDict1 = dict()
myDict2 = dict()
for i in range(n):
    syn = list(input().split())
    for word in syn:
        if word not in myDict1:
            myDict1[syn[1]] = syn[0]
        if word not in myDict2:
            myDict2[syn[0]] = syn[1]
w = input()
if w in myDict1:
    print(myDict1[w])
elif w in myDict2:
    print(myDict2[w])
