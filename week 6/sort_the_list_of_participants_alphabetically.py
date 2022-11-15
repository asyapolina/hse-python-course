inFile = open("input.txt", "r", encoding="utf8")
outFile = open("output.txt", "w", encoding="utf8")
data_sorted = sorted(inFile)
for line in data_sorted:
    data = line.split()
    print(*data[0:2], data[-1], file=outFile)
inFile.close()
outFile.close()
