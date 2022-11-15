inFile = open("input.txt", "r", encoding="utf8")
myDict = dict()
lines = inFile.readlines()
for line in lines:
    for word in line.split():
        if word not in myDict:
            myDict[word] = 1
        else:
            myDict[word] += 1
new_dict = sorted(myDict.keys(), key=lambda x: x.lower())
max_key = max(new_dict, key=myDict.get)
print(max_key)
inFile.close()
