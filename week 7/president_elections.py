in_file = open("input.txt", "r", encoding="utf8")
out_file = open("output.txt", "w", encoding="utf8")
lines = in_file.readlines()
candidates = dict()
for name in lines:
    name = name.rstrip()
    candidates[name] = candidates.get(name, 0) + 1
sorted_cand = sorted(candidates.items(), key=lambda x: x[1], reverse=True)
if sorted_cand[0][1] > len(lines) / 2:
    print(sorted_cand[0][0], file=out_file)
else:
    print(sorted_cand[0][0], sorted_cand[1][0], sep="\n", file=out_file)
in_file.close()
out_file.close()
