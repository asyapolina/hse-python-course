inFile = open("input.txt", "r", encoding="utf8")
myDict = dict()
s = ""
for line in inFile:
    for word in line.split():
        if word not in myDict:
            myDict[word] = 0
        else:
            myDict[word] += 1
        s += str(myDict[word]) + " "
print(s)
inFile.close()
