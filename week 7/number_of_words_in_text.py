in_file = open("input.txt", "r", encoding="utf8")
my_set = set()
count = 0
for line in in_file:
    for word in line.split():
        if word not in my_set:
            my_set.add(word)
print(len(my_set))
in_file.close()
