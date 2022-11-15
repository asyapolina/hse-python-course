n = int(input())
list_of_participance = []
lst9 = []
lst10 = []
lst11 = []
for i in range(n):
    m = list(input().split())
    list_of_participance.append(m)
for j in range(len(list_of_participance)):
    if list_of_participance[j][2] == "9":
        lst9.append(list_of_participance[j])
    elif  list_of_participance[j][2] == "10":
        lst10.append(list_of_participance[j])
    elif list_of_participance[j][2] == "11":
        lst11.append(list_of_participance[j])

#sorted_list_particip = sorted(list_of_participance, key=lambda x: (int(x[2]), int(x[3])))

# for i in range(len(reversed_list_particip)):
##     print(reversed_list_particip[i][0])