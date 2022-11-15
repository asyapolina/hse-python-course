inFile = open("input.txt", "r", encoding="utf8")
outFile = open("output.txt", "w", encoding="utf8")
lines = inFile.readlines()
passed_score40 = []
score = 0
lst_of_passed40 = []
k = int(lines[0])
for ch in lines[1:]:
    ch = ch.split()
    if int(ch[-1]) > 39 and int(ch[-2]) > 39 and int(ch[-3]) > 39:
        passed_score40.append(ch)
for j in passed_score40:
    score = int(j[-1]) + int(j[-2]) + int(j[-3])
    lst_of_passed40.append(score)
lst_passed_40sc = sorted(lst_of_passed40, reverse=True)
if len(lst_of_passed40) <= k or k == 0:
    print(0)
elif lst_of_passed40.count(max(lst_of_passed40)) > k:
    print(1)
elif lst_passed_40sc[k] == lst_passed_40sc[k - 1]:
    print(lst_passed_40sc[lst_passed_40sc.index(lst_passed_40sc[k]) - 1])
else:
    print(lst_passed_40sc[k - 1])
inFile.close()
outFile.close()
