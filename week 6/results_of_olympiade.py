n = int(input())
list_of_participance = []
for i in range(n):
    m = list(input().split())
    list_of_participance.append(m)
sort_list_particip = sorted(list_of_participance, key=lambda x: int(x[1]))
reversed_list_particip = sort_list_particip[::-1]
for i in range(len(reversed_list_particip)):
    print(reversed_list_particip[i][0])
