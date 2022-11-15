with open('input.txt', 'r', encoding='utf8') as inF:
    lines = inF.readlines()
outF = open('output.txt', 'w', encoding='utf8')
Pl, Scr = [], []
for line in lines:
    Pl.append(list((line.split())[-3:]))
K = int(*Pl[0])
for i in range(1, len(Pl)):
    if int(Pl[i][0]) > 39 < int(Pl[i][1]) > 39 < int(Pl[i][2]):
        Scr.append((int(Pl[i][0]) + int(Pl[i][1]) + int(Pl[i][2])))
Scr.sort(key=lambda x: -x)
if K >= len(Scr) or K == 0:
    print(0)
elif Scr.count(max(Scr)) > K:
    print(1)
elif Scr[K] == Scr[K - 1]:
    print(Scr[Scr.index(Scr[K]) - 1])
else:
    print(Scr[K - 1])
outF.close()
