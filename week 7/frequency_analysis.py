inFile = open("input.txt", "r", encoding="utf8")
myDict = dict()
for line in inFile:
    for word in line.split():
        if word not in myDict:
            myDict[word] = 1
        else:
            myDict[word] += 1
sorted_by_keys = sorted(myDict.items())
sorted_by_v_and_k = sorted(sorted_by_keys, key=lambda x: x[1], reverse=True)
for i in sorted_by_v_and_k:
    print(i[0])
inFile.close()
