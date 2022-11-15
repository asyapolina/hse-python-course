n = int(input())
common_lang = set()
unique_lang = set()
for i in range(n):
    a = int(input())
    pupil_lang = set()
    for el in range(a):
        language = input()
        pupil_lang.add(language)
    if i == 0:
        common_lang = pupil_lang
    else:
        common_lang &= pupil_lang
    unique_lang |= pupil_lang
print(len(common_lang))
for j in common_lang:
    print(j)
print(len(unique_lang))
for g in unique_lang:
    print(g)
