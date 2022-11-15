lst = list(map(int, input().split()))
empty_space = lst[0]
n_users = lst[1]
users_data = []
for i in range(n_users):
    a = int(input())
    users_data.append(a)
users_data.sort()
a_sum = 0
count = 0
for j in range(len(users_data)):
    if a_sum <= empty_space - users_data[j]:
        a_sum += users_data[j]
        count += 1
    else:
        break
print(count)
